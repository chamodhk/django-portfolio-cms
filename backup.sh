#!/bin/sh
set -eu

APP_DIR=/opt/personal-website
BACKUP_DIR=/var/backups/personal-website
STAMP=$(date -u +%Y-%m-%dT%H%M%SZ)
DEST="$BACKUP_DIR/$STAMP"

mkdir -p "$DEST"
cd "$APP_DIR"

docker compose -f docker-compose.prod.yml exec -T web \
  python manage.py dumpdata --natural-foreign --natural-primary \
  | gzip > "$DEST/django-data.json.gz"

docker compose -f docker-compose.prod.yml exec -T web python -c \
  "import sqlite3; src=sqlite3.connect('/app/db/db.sqlite3'); dst=sqlite3.connect('/tmp/db.sqlite3'); src.backup(dst); dst.close(); src.close()"
docker cp personal-website-web-1:/tmp/db.sqlite3 "$DEST/db.sqlite3"
docker compose -f docker-compose.prod.yml exec -T web rm -f /tmp/db.sqlite3

docker run --rm -v personal-website_media:/media:ro alpine \
  tar -czf - -C /media . > "$DEST/media.tar.gz"


find "$BACKUP_DIR" -mindepth 1 -maxdepth 1 -type d -mtime +6 -exec rm -rf -- {} +

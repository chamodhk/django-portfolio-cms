# Django Portfolio CMS

A portfolio and blog built with Django and Tailwind CSS. Content can be managed through the Django admin panel.

## Run locally

Create a `.env` file, then run:

```sh
docker compose up --build
```

The site will be available at `http://localhost:8000`.

## Manage content

Create an admin user:

```sh
docker compose exec web python manage.py createsuperuser
```

Then open `http://localhost:8000/admin/`. From the admin panel you can update site settings, publish articles, add projects and skills, manage certificates, and upload images or a résumé without changing the code.

On production, use:

```sh
docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

Then sign in at `/admin/` on your domain.

## Production

The production setup uses Docker Compose, Gunicorn, Caddy, automatic HTTPS, persistent SQLite and media volumes, and nightly backups.

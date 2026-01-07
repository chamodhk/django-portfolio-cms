from datetime import timedelta
from django.db.models import F 
from django.utils import timezone
from main.models import Article 

VIEW_COOLDOWN = timedelta(hours=12)

def register_article_view(request, article_id):
    viewed_articles = request.session.get("viewed_articles", {})


    now = timezone.now()

    last_viewed = viewed_articles.get(str(article_id))

    if last_viewed:
        last_viewed_time = timezone.datetime.fromisoformat(last_viewed)

        if now - last_viewed_time < VIEW_COOLDOWN:
            return False 


    Article.objects.filter(pk=article_id).update(
        view_count=F("view_count") + 1
    )

    viewed_articles[str(article_id)] = now.isoformat()
    request.session["viewed_articles"] = viewed_articles

    return True
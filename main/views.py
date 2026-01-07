import os 
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import SiteSettings, Article, Project, Skill, Certificate, SiteSettings
from .services.article_views import register_article_view
from .forms import CommentForm
from django.db.models import Q


# Create your views here.


def home(request):
    settings = SiteSettings.objects.first()
    if settings:
        article = Article.objects.order_by('-date').first()
        return render(request, "home.html", {
            "settings": settings,
            "article":article
        })
    else:
        return render(request, "installed.html")


def blog_home(request):

    articles = Article.objects.all().order_by('-date')
    query = request.GET.get("q", "")
    tag_query = request.GET.get("tag","")

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(body__icontains=query)
        )

    if tag_query:
        articles = articles.filter(
            tags__name__in=[tag_query]
        ).distinct()

    paginator = Paginator(articles,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"bloghome.html", {"page":page, "query":query, "tag_query": tag_query})

def get_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    comment_form = CommentForm(request.POST or None)

    if request.method == "POST" and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

        return redirect(
            f"{request.path}?comment_submitted=1#comments"
        )

    if request.method == "GET":
        register_article_view(request, article.pk)
        article.refresh_from_db(fields=["view_count"])

    recent_articles = Article.objects.order_by("-date")[:4]

    comments = article.comments.filter(
        is_approved=True
    )

    return render(
        request,
        "post.html",
        {
            "article": article,
            "recents": recent_articles,
            "comments": comments,
            "comment_form": comment_form,
            "comment_submitted": (
                request.GET.get("comment_submitted") == "1"
            ),
        },
    )
def projects(request):
    projects = Project.objects.prefetch_related("skills")
    skills = Skill.objects.all()
    return render(request, "projects.html",context={
        "projects":projects,
        "skills":skills
    })


def achievements(request):
    certificates = Certificate.objects.prefetch_related('skills').order_by('-issued_date')
    return render(request, "achievements.html", {"certificates": certificates})


def ads_txt_view(request):
    with open(os.path.join(settings.STATIC_ROOT,'ads.txt')) as file:
        file_content = file.readlines()
    return HttpResponse(file_content, content_type="text/plain")

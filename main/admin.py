from django.contrib import admin
from django.db import models
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ArticleModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(SiteSettings)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "article",
        "created_date_time",
        "is_approved",
    )
    list_filter = (
        "is_approved",
        "created_date_time",
    )
    search_fields = (
        "name",
        "body",
        "article__title",
    )
    list_editable = ("is_approved",)


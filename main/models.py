from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


# Create your models here.

class Skill(models.Model):
    SKILL_TYPES = [
        ("language", "Programming Language"),
        ("framework", "Framework"),
        ("tool", "Tool"),
        ("soft", "Soft Skill"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=SKILL_TYPES)
    icon_slug = models.CharField(
        max_length=50,
        help_text="Simple Icon's icon slug",
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    institute = models.CharField(max_length=50)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="certificates")

    def __str__(self) -> str:
        return f"{self.name} from {self.institute}"
    

class Project(models.Model):
    PROJECT_CATEGORIES = [
        ("academic", "Academic"),
        ("personal", "Personal / Hobby"),
        ("research", "Research"),
        ("open_source", "Open Source"),
        ("experimental", "Experimental"),
        ("freelance", "Freelance / Client"),
        ("learning", "Learning / Practice"),
    ]


    name = models.CharField(max_length=150)
    description = models.TextField()
    completed_date = models.DateField()
    category = models.CharField(max_length=30, choices=PROJECT_CATEGORIES, default="personal")
    article_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name="projects")

    tags = TaggableManager(blank=True)

    thumbnail = models.ImageField(
        upload_to="project_thumbnails/",
        blank=True,
        null=True,
        help_text="Project cover image"
    )

    # for SEO

    meta_title = models.CharField(
        max_length=60,
        blank= True,
        help_text="Leave empty to use article title"
    )

    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="short summary for Google search results"
    )


    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    date = models.DateTimeField()
    slug=AutoSlugField(populate_from='title', unique_with="date__month")


    body = models.TextField()

    tags = TaggableManager(blank=True)
    medium_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)


    view_count = models.IntegerField(default=0)
    claps = models.IntegerField(default=0)


    # for SEO

    meta_title = models.CharField(
        max_length=60,
        blank= True,
        help_text="Leave empty to use article title"
    )

    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="short summary for Google search results"
    )


   

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=1000)
    created_date_time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_date_time"]

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"

class SiteSettings(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    subtitle = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    last_update = models.DateField(auto_now=True)

    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)


    def __str__(self) -> str:
        return "Site Settings"


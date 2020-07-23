from django.contrib import admin
from articles.models import Topic, Article, Comment


@admin.register(Topic)
class TopicModelAdmin(admin.ModelAdmin):
    verbose_name = "topic"
    verbose_name_plural = "topics"
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    verbose_name = "article"
    verbose_name_plural = "articles"
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Comment)

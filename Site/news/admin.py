from django.contrib import admin
from .models import Article
from modeltranslation.admin import TranslationAdmin
@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',) }
    prepopulated_fields = {'url': ('slug',) }
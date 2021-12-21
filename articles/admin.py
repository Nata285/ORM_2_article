from turtle import title


from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.forms import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article,Topic,Position

class PositionInlineformset(BaseInlineFormSet):
    pass

class PositionsInline(admin.TabularInline):
    model = Position
    formset = PositionInlineformset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','text','published_at']
    inlines = [PositionsInline]


@admin.register(Topic)
class TopicAdmin (admin.ModelAdmin):
    list_display = ['id', 'name']





from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from parler.admin import TranslatableAdmin
from .models import Announcement, Category, Response

@admin.register(Announcement)
class AnnouncementAdmin(TranslatableAdmin):
    list_display = ('title', 'get_category', 'date_in')
    list_filter = ('category', 'date_in')
    search_fields = ('translations__title', 'translations__content')

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = 'Категория'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('content', 'user')
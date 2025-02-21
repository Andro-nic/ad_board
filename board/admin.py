from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from parler.admin import TranslatableAdmin
from .models import Announcement, Category, Response

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category', 'date_in')
    list_filter = ('category', 'date_in')
    search_fields = ('title', 'content')

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = 'Категория'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('content')


# Регистрируем модели для перевода в админке

class CategoryAdmin(TranslationAdmin):
    model = Category


class AnnouncementAdmin(TranslationAdmin):
    model = Announcement


class ResponseAdmin(TranslationAdmin):
    model = Response


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Response, ResponseAdmin)
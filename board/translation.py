from .models import Category, Announcement, Response
from modeltranslation.translator import register, TranslationOptions
# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


# регистрируем наши модели для перевода

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
   fields = ('title', 'content',)


@register(Response)
class ResponseTranslationOptions(TranslationOptions):
    fields = ('content',)
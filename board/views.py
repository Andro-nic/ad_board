from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Announcement, Response
from .forms import ResponseForm
from django.shortcuts import get_object_or_404, redirect
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from .forms import AnnouncementForm


class AnnouncementsList(ListView):
    model = Announcement
    ordering = ['-date_in']
    template_name = 'announcements.html'
    context_object_name = 'announcements'
    paginate_by = 5


class AnnouncementDetail(DetailView):
    template_name = 'announcement.html'
    queryset = Announcement.objects.all()

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта
        obj = cache.get(f'announcement-{self.kwargs["pk"]}', None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.
        # если объект' нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'announcement-{self.kwargs["pk"]}', obj)
        return obj


class CreateAnnouncementView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm  # Используем вашу форму с TinyMCE
    template_name = 'create_announcement.html'
    success_url = reverse_lazy('announcement_list')
    success_msg = 'Объявление создано'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Устанавливаем текущего пользователя как автора
        return super().form_valid(form)


class ResponseToAnnouncementView(LoginRequiredMixin, CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'create_response.html'
    success_msg = 'Отклик создан'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.announcement = get_object_or_404(Announcement, id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.kwargs['pk']})


class UserResponsesView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'user_responses.html'
    context_object_name = 'responses'
    ordering = ['-date_in']
    paginate_by = 5

    def get_queryset(self):
        # Фильтруем отклики по объявлениям текущего пользователя
        return Response.objects.filter(announcement__user=self.request.user)


class AcceptResponseView(LoginRequiredMixin, UpdateView):
    model = Response
    fields = []
    template_name = 'response_accept.html'

    def post(self, request, *args, **kwargs):
        response = self.get_object()
        response.is_accepted = True
        response.save()

        # Отправка email пользователю, оставившему отклик
        send_mail(
            'Ваш отклик принят',
            f'Ваш отклик на объявление "{response.announcement.title}" был принят.',
            'AndrSFtest@yandex.ru',
            [response.user.email],

            fail_silently=False,
        )

        return redirect('user_responses')


class DeleteResponseView(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'response_confirm_delete.html'
    success_url = reverse_lazy('user_responses')


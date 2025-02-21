from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user  # Передаем текущего пользователя в контекст
    #     context['user_id'] = self.request.user.id  # Передаем ID пользователя в контекст
    #     return context





from django.urls import path, include
from .views import UserResponsesView

from .views import (CreateAnnouncementView, ResponseToAnnouncementView,
                    AnnouncementsList, AnnouncementDetail, AcceptResponseView, DeleteResponseView)


urlpatterns = [
    path('', AnnouncementsList.as_view(), name='announcement_list'),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('announcement/new/', CreateAnnouncementView.as_view(), name='create_announcement'),
    path('<int:pk>/response/', ResponseToAnnouncementView.as_view(), name='response_create'),
    path('responses/', UserResponsesView.as_view(), name='user_responses'),
    path('response/<int:pk>/accept/', AcceptResponseView.as_view(), name='accept_response'),
    path('response/<int:pk>/delete/', DeleteResponseView.as_view(), name='delete_response'),
    path('tinymce/', include('tinymce.urls')),
]
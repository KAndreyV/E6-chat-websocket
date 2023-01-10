# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("chats/", views.index, name="index"),
    path("chats/<str:room_name>/", views.room, name="room"),
    path('writers/writers/', views.WritersList.as_view(), name='users_list'),
    path('writers/<int:pk>/', views.WriterDetail.as_view(), name='user_detail'),
    path('writers/<int:pk>/upgrade/', views.WriterUpgrade.as_view(), name='writer_edit'),
    path('', views.RoomList.as_view()),
    path('<int:pk>/', views.RoomDetail.as_view()),
]

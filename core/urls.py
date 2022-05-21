from django.urls import path

from .views import *

urlpatterns = [
	path('chat/<int:pk>', chat, name = 'chat'),
	path('leave_chat', leave_chat, name = 'leave_chat'),
	path('add_message/', add_message, name = 'add_message'),
	path('get_or_create_chat/', get_or_create_chat, name = 'get_or_create_chat'),
]
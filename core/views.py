from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import *


def chat(request, pk):

	curent_chat = Chat.objects.get(id = pk)

	all_users = User.objects.all()

	user_chats = [] 
	users = []

	chats = Chat.objects.all()

	search = request.GET.get('search', '')

	for chat in chats:
		for chat_user in chat.users.all():
			if chat_user.id == request.user.id:
				user_chats.append(chat)	

	if search:
		for user_chat in user_chats:
			for user in user_chat.users.all():
				if user.username == search:
					users.append(user_chat)
		user_chats = users

	context = {
		'curent_chat' : curent_chat,
		'user_chats' : user_chats,
		'users' : all_users
	}

	return render(request, 'index.html', context)


def get_or_create_chat(request):

	user_id = request.GET.get('user_id')
	user_taken = User.objects.get(id = user_id)

	chats = Chat.objects.all()

	for chat in chats:
		for user in chat.users.all():
			if user == user_taken:
				curent_chat = Chat.objects.get(id = chat.id)
				curent_chat.users.add(request.user)

				return redirect('chat', pk = curent_chat.id)

	curent_chat = Chat.objects.create()
	curent_chat.users.add(user_taken)
	curent_chat.users.add(request.user)
	curent_chat.save()

	return redirect('chat', pk = curent_chat.id)


def leave_chat(request):

	chat_id = request.GET.get('chat_id')
	curent_chat = Chat.objects.get(id = chat_id)

	curent_chat.users.remove(request.user)

	return redirect(request.META['HTTP_REFERER'])


def add_message(request):

	if request.method == 'POST':

		chat_id = request.POST.get('chat_id')
		body = request.POST.get('body')

		curent_chat = Chat.objects.get(id = chat_id)

		message = Message.objects.create(user = request.user, body = body)

		curent_chat.messages.add(message)
		curent_chat.save()

	return redirect('chat', pk = chat_id)
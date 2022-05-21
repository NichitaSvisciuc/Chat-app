from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Message(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.user.username}'s message"

class Chat(models.Model):

	users = models.ManyToManyField(User)
	messages = models.ManyToManyField(Message)

	def __str__(self):
		usernames = ''

		for user in self.users.all():
			usernames += user.username + ', '

		return f"{usernames}'s chat"

	def get_absolute_url(self):
		return reverse('chat', kwargs = {
				'pk' : self.id,
			})
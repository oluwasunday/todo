from .models import *
from django.forms import ModelForm
from django import forms


class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add New Task...'}))

	class Meta:
		model = Task
		fields = '__all__'
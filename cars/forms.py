from django import forms

from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        # fields = '__all__'
        fields = ['brand', 'name', 'description', 'image', 'price', 'quantity']


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        # fields = '__all__'
        fields = ['name', 'email', 'body']

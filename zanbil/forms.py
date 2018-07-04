from django.forms import ModelForm

from .models import Review, Business, Test


class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'category', 'email', 'phone_number', 'address']

class testForm(ModelForm):
    class Meta:
        model = Business
        fields = ['image']
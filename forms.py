from django import forms


class Bookingform(forms.Form):
	name=forms.CharField(max_length=50)
	age=forms.IntegerField()
	email=forms.EmailField()
	profile=forms.FileField()

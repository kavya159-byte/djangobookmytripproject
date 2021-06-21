from django.shortcuts import render
from Booking.models  import Book
from . import forms
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings





# Create your views here.
def function(request):
	
	return render(request,'index.html')  

def about(request):
	return render(request,'about.html')

def services(request):
	return render(request,'services.html')

def booking(request):
	var=Book.objects.all()
	return render(request,'booking.html',{'book':var})


def sucess(request):
	return render(request,'sucess.html')


def bookingform(request):
	if request.method=='POST':
		subject="Dear USER"
		body="We recieved you Application, Our Respresentative will get back to you within 24 hours"
													
		message=send_mail(subject,body,settings.EMAIL_HOST_USER,[request.POST.get('email'),])
		return render(request,'sucess.html')
	return render(request,'bookingform.html')











 


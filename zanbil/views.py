from django.http import HttpResponse
from django.shortcuts import render
from .forms import testForm
from .models import Categories, Services, Reserves, Review, Business, Sans, Users ,Test
from django.shortcuts import redirect
from khayyam import *

# Create your views here.

categories = Categories.objects.all()
user = Users.objects.get(id=1)

def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})

def test(request):
    return render(request,'service.html')

def form (request,id):
    if request.method == 'POST':
        form = testForm(request.POST, request.FILES)
        if form.is_valid():
            savedBusiness = Business.objects.get(pk=id) 
            business = form.save(commit=False)
            savedBusiness.image = business.image
            savedBusiness.save()
            return redirect('BusinessPage', id)
        else:
            print('ridi')
    else:
        form = testForm()
    return render(request,'uploadPhotoForm.html', {'id':id})

def imagetest(request,id):
    testt = Test.objects.get(pk=id)
    return render(request,'showtest.html',{'test':testt})
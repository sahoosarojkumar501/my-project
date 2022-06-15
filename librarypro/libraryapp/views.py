from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Details_of_book,Login_page
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import *
from django import forms


# Create your views here.
def Book_Details(request):
    if request.method=='GET':
        ob=Details_of_book.objects.all()
        return render (request,'details.html',{'ob':ob})

def login_page(request):
    if request.method=='GET':
        return render(request,'home.html')
    else:
        '''Login_page(
        email=request.POST['emails'],
        password=request.POST['passwords']
        ).save()
        return redirect('main_page')
        '''
        email=request.POST['email']
        password=request.POST['passwords']
        username = User.objects.get(email=email.lower()).username

        user=authenticate(username=username,password=password)
        print(request.POST['email'])
        if user:
            if user.is_active:
                login(request,user)
                return redirect('main_page')
        return HttpResponse('worng password')

def Add_book(request):
    if request.method=='GET':
        return render (request,'forms.html')
    else:
        Details_of_book(
        book_name=request.POST.get('fname'),
        author_name=request.POST.get('aname'),
        publisher_name=request.POST.get('pname'),
        email_id=request.POST.get('email'),
        price=request.POST.get('price')
        ).save()
        return redirect('main_page')

def update_data(request,id):
    updates = Details_of_book.objects.get(id=id)
    return render(request,'update_data.html',{'updates':updates})

def save_update_data(request,id):
    updates=Details_of_book.objects.get(id=id)
    updates.book_name=request.POST.get('fname')
    updates.author_name=request.POST.get('aname')
    updates.publisher_name=request.POST.get('pname')
    updates.email_id=request.POST.get('email')
    updates.price=request.POST.get('price')
    updates.save()
    return redirect('main_page')

def delete_data(request,id):
    updates=Details_of_book.objects.get(id=id)
    updates.delete()
    return redirect ('main_page')

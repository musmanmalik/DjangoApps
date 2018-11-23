from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView
from rest_framework import serializers

from .models import Product, Comment, Rating
from .forms import RegisterForm
import requests


class Homeview(generic.ListView):
    template_name = 'product/Home.html'
    context_object_name = 'products'
    """Getting data using api"""
    def get_queryset(self):
    #     return Product.objects.all()
    #getting data using api
        response = requests.get('http://127.0.0.1:8000/api/products')
        print(response)
        return response.json()


class ProductUpdate(UpdateView):
        model = Product
        fields = ['Name', 'Price', 'Description', 'UpdatedBy', 'PicUrl']
        success_url = reverse_lazy('home')


class ProfileUpdate(UpdateView):
    template_name = 'product/SignUp.html'
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('home')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('home')


class Addproduct(CreateView):

    model = Product
    fields = ['Name', 'Price', 'Type', 'Description', 'UpdatedBy', 'PicUrl']
    success_url = reverse_lazy('home')


def login1(request):
    if request.method == 'POST':
        data = request.POST.dict()
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "User not Exist"
            return redirect('home')
    else:
       return render(request,'product/Home.html',{'products':Product.objects.all()})


def logout1(request):
    logout(request)
    return redirect('home')


class SignUpView(generic.View):
    template_name = 'product/Home.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned(Normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            # SignUp Using api
           # response = requests.post('http://127.0.0.1:8000/api/signup', data={'username': username, 'password': password, 'email': email})
            user = authenticate(username=username, password=password)
            if user is not None:
                user.email = email
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        return render(request, self.template_name, {'form': form})


def Comment1(request, product_id):
    if request.method == 'POST':
        data = request.POST.dict()
        obj = Comment()
        obj.comment = data['comment']
        obj.product = product_id
        obj.save()
        return redirect('home')


def send_to_Home(request):
    return redirect('/')


def getcomment(request):
    print("function called")
    id = request.GET.get('product_id', None)
    try:
        obj = Comment.objects.filter(product=id)
    except Comment.DoesNotExist:
        raise ObjectDoesNotExist(('no product found for this id {}'.format(id)))

    data1 = []
    for proj in obj:
        data1.append(proj.comment)
    data = {
        'comments':data1
    }
    return JsonResponse(data)


def sendtofriend(request, product_id):
    if request.method == 'POST':
        data = request.POST.dict()
        email = data['email']
        obj = Product.objects.filter(id=product_id).first()
        # send_mail('Product Invitation', 'This good is good for you: ' + str(obj.Name), email,
        #           [email], fail_silently=True)
        subject = "Product Invitation"
        message = "This is Good For You"
        from_email = email
        send_mail(subject,message,from_email,[from_email],fail_silently=True)
        return redirect('home')
    else:
        return redirect('home')


def getrate(request):
    id = request.GET.get('product_id', None)
    new_rate = request.GET.get('value', None)
    obj = Rating.objects.filter(product_id=id).first()
    t_point = float(obj.t_point) + 1
    obj.t_point = t_point
    o_point = float(obj.o_points) + float(new_rate)
    obj.o_points = o_point/t_point
    obj.save()

    data = {
        'u_rate': str(round(o_point/t_point, 2))
    }
    return JsonResponse(data)







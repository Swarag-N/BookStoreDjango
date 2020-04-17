from django.shortcuts import render,redirect,get_list_or_404

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages import add_message, constants

from django.views import View
from django.views.generic import ListView
from django import forms
from django.forms import ModelForm
from .models import Book, Order



class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields= ['books']
        # exclude = ['customer']
        widgets = {"books":forms.CheckboxSelectMultiple()}

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','password1','password2']


class SignUpView(View):

    def get(self,request):
        user_form = SignUpForm()
        return render(request, 'auth/signup.html',{'form':user_form})

    def post(self,request):
        form_data = SignUpForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            op = form_data.cleaned_data
            user = authenticate(username=op['username'],password=op['password1'])
            login(request,user)
            return redirect('home')
        else:
            add_message(request,constants.ERROR,form_data.errors.as_ul())
            return redirect('signup')

        return render(request,'auth/login.html',{'form':form_data})
        

class ShowBooks(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model=Book
    template_name = 'store/books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=OrderForm()
        return context
    
    def post(self, request):
        temp_order = Order(customer=request.user)
        order_form = OrderForm(data = request.POST,instance=temp_order)
        if order_form.is_valid():
            order_form.save(request.user)
            add_message(request,constants.SUCCESS,"Succes")
            return render(request,'base.html')
        else:
            add_message(request,constants.WARNING,"there was an error")
            return render(request,'base.html')
        return render(request,'base.html')



class OrderBooks(LoginRequiredMixin,ListView):
    model = Order
    template_name='store/orders.html'
    # queryset = Order.objects.filter(customer=request.user)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(customer=self.request.user)
        # self.customer = get_list_or_404(Order, customer=self.request.user)
        # return [i.books.all() for i in Order.objects.filter(customer=self.request.user)]
    
    def get_context_data(self):
        data = super().get_context_data()
        cd = data['order_list']
        # data['books_list']
        return data


    



class HomeView(View):
    def get(self,request):
        return render(request,'base.html')

# Create your views here.

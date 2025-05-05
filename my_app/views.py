from django.shortcuts import render, redirect

from my_app.models import Customer
from my_app.my_forms import CustomerForm


# Create your views here.
def home(request):
    if request.method=="POST":
        names= request.POST.get('names')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        password= request.POST.get('password')
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        gender=request.POST.get('gender')
        print(names,email,phone,password,weight,height,gender)
        Customer.objects.create(name=names,email=email,phone=phone,password=password,weight=weight,height=height,gender=gender)
        count=Customer.objects.all().count()
        print(f"{count} Customers")

    return render(request, 'home.html')


def show(request):
    data=Customer.objects.all().order_by('-id') # select * from customers
    return render(request, 'show.html' ,{'data':data})


def delete(request,id):
    user=Customer.objects.get(id=id)
    user.delete()
    return redirect('show-page')


def details(request,id):
    user=Customer.objects.get(id=id)
    return render (request,'details.html',{'user':user})


def add(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-page')
    else:
        form = CustomerForm()
    return render(request,'forms.html',{'form':form})
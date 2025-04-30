from django.shortcuts import render

from my_app.models import Customer


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
    data=Customer.objects.all()
    return render(request, 'show.html' ,{'data':data})
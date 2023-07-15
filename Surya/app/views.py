from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Contact


    

def home(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']
        cot= Contact(name=name,email=email,subject=subject,message=message)
        cot.save()
        message="message sended"
        context = {
             'message':message,
        }
        return render(request,'status.html',context)
    else:
        context = {
        }
        return render(request,'contact.html',context)
    

def getaquote(request):
    return render(request,'get-a-quote.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def sampleinnerpage(request):
    return render(request,'sample-inner-page.html',{})

def servicedetails(request):
    return render(request,'service-details.html',{})

def services(request):
    return render(request,'services.html',{})

def view(request):
    cont= Contact.objects.all()
    context = {
        'cont': cont
    }
    return render(request, 'view.html', context)










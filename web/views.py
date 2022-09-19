from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    return render(request,'web/home.html')

def about(request):
    return render(request,'web/about.html')

def contact(request):
    return render(request,'web/contact.html')
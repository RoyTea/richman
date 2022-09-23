from django.shortcuts import render

import builds

# Create your views here.

def homepage(request):
    return render(request, 'builds/index.html')

def about(request):
    return render(request, 'builds/about.html')

def contact(request):
    return render(request, 'builds/contact.html')

def gallerysingle(request):
    return render(request, 'builds/gallery-single.html')

def gallery(request):
    return render(request, 'builds/gallery.html')

def sampleinnerpage(request):
    return render(request, 'builds/sample-inner-page.html')

def services(request):
    return render(request, 'builds/services.html')
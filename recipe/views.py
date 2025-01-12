from django.shortcuts import render
from django.contrib import messages
from recipe.forms import ContactForm , AboutFrom


def home_page(request):
    return render(request,'index.html')

def about_page_view(request):

    if request.method == "GET":
        return render(request,'pages/about.html')
    elif request.method == "POST":
        form = AboutFrom(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request,'pages/about.html')
        else:
            context = {
                "errors":form.errors
            }
            return render(request,'pages/about.html',context)


def contact_page_view(request):
    
    if request.method == "GET":
        return render(request,'pages/contact.html')
    
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your contact information is sent to database')
            return render(request,'pages/contact.html')
        else:
            context = {
                "errors":form.errors
            }
            messages.error(request,'Something getting wrong , please again later')
            return render(request,'pages/contact.html',context)
      

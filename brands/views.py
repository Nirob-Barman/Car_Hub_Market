from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def add_brands(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.BrandForm(request.POST)
            if form.is_valid():
                # confusion
                # form.instance.user = request.user
                form.instance.author = request.user
                form.save()
                return redirect('home')
        else:
            form = forms.BrandForm()
        return render(request, 'form.html', {'form': form, 'title': 'Add Brand', 'button_text': 'Add Brand', 'button_class': 'btn-success'})
    else:
        return redirect('login')

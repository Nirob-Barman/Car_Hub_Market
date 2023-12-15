from django.shortcuts import render, redirect
from . import forms

# Create your views here.


def add_brands(request):
    if request.method == 'POST':
        form = forms.BrandForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = forms.BrandForm()

    return render(request, 'form.html', {'form': form, 'title': 'Add Brand', 'button_text': 'Add Brand', 'button_class': 'btn-success'})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ImageForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def test1(request):
    return render(request, 'Test1.html')

@login_required
def test2(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'Test2.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'Test2.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



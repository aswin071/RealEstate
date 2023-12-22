from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm



@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)  
                return redirect('property_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

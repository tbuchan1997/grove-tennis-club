from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterUserForm

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_slot')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})
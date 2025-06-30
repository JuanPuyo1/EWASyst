from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

class LoginModifiedView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                return redirect('accounts:login')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class ProfileView(View):
    template_name = 'accounts/profile.html'
    form_class = ProfileForm
    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST, instance=request.user) #instance=request.user es para que el formulario se llene con los datos del usuario actual
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('accounts:profile' )
        else:
            messages.error(request, 'Error al actualizar el perfil')
        return render(request, self.template_name, {'form': form})
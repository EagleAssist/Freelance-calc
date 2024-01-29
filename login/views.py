from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django import forms
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'location']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationView(View):
    template_name = 'register.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user=form.save()
        else:
            return HttpResponse("form error")
            
            
            
        return HttpResponse("reg okay")
    
class UserLoginView(View):
    template_name = 'login.html'
    default_redirect_url = 'api/calculate/'

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # form = CustomAuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     # user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        #     user = CustomUser.objects.get(username=form.cleaned_data['username'])
        #     # if check_password(form.cleaned_data['password'], user.password):
        #     #     pass
        #     # else:
        #     #     return HttpResponse('password error')
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                
                login(request, user)
                next_url = request.GET.get('next', self.default_redirect_url)
                

                return redirect(next_url)
            else:
                return HttpResponse("auth error")
        # return render(request, self.template_name, {'form': form})
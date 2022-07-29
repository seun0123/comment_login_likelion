from django.shortcuts import render, redirect
# 장고에서 제공하는 auth 기능
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
# 회원가입
def signup(request) : 
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if request.POST["password1"] == request.POST["password2"] :
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password1"]
            )
            nickname = request.POST["nickname"],
            age = request.POST["age"],
            phone_num = request.POST["phone_num"],
            email = request.POST["email"]
            profile = Profile(user=user, nickname=nickname, age=age, phone_num=phone_num, email=email)
            profile.save()
            auth.login(request, user)
            return redirect('main')
            # return redirect('myapp/main')
        else :
            return render(request, 'account/signup.html', {'form':form})
    else :
        form = UserCreationForm()
        return render(request, 'account/signup.html', {'form':form})

# 로그인
def login(request):
    if request.method == 'POST' :
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
            # return redirect('myapp/main')
        else:
            return render(request, 'account/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form':form})

# 로그아웃
def logout(request) :
    auth.logout(request)
    return redirect('main')
    # return redirect('myapp/main')

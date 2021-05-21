from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # AuthenticationForm는 로그인을 해주는 form, UserCreationForm은 회원가입을 해주는 form
from django.contrib.auth import authenticate, login, logout  # 회원가입 할 때 여기까지는 필수
from .forms import RegisterForm  # 장고에서 지원해주는 form 사용
# Create your views here.

def login_view(request): # login 담당 함수
    if request.method == 'POST':   # 데이터베이스와 관련된 것은 POST 방식으로 렌더링
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid(): #유효성 검사 통과하면 username 변수를 만들어줌.
            username = form.cleaned_data.get("username") # clean한 데이터의 username이라는 것을 가져와서 변수에 저장
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)  # 인증을 받는 객체, username, password는 form에서 받은 정보, 이것을 인증을 받음.

            if user is not None:  #user가 존재할때 로그인
                login(request, user)
        return redirect("homeHtml")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
  
def logout_view(request):  # logout 담당 함수
    logout(request)
    return redirect("homeHtml")    

def register_view(request):
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # commit이 들어갈 필요없음.
            login(request, user)
        return redirect('homeHtml')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})


  
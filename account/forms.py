from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm): # UserCreationForm을 상속을 통해 기능들을 모두 상속받음.
    class Meta:  # CustomUser에 맞는 회원가입 form이 완성됨.
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'tel', 'email', 'university', 'address']  # 추가한 colmn을 home으로 보냄.
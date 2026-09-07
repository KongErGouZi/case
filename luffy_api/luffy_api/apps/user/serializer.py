from rest_framework import serializers
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
import re
from .models import User
from rest_framework.exceptions import APIException
from typing import Dict, Any
from django.core.cache import cache


class LoginSerializer(serializers.Serializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        user = self._get_user(attrs)
        token = self._get_token(user)
        self._pre_data(user, token)

        return attrs

    def _get_user(self, attrs: Dict[str, Any]) -> User:
        raise NotImplementedError('子类必须实现 _get_user 方法')

    def _get_token(self, user: User) -> str:
        """ 根据User实例，签发token，返回token令牌 """
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def _pre_data(self, user: User, token: str) -> None:
        """ 将查询到的用户名、token、头像放入context中，实现序列化类和视图类之间通信 """
        self.context['username'] = user.username
        self.context['token'] = token
        self.context['icon'] = settings.BACKEND_URL + '/media/' + str(user.icon)


class MulLoginSerializer(LoginSerializer):
    # 自定义字段
    username = serializers.CharField(max_length=12, min_length=2)
    password = serializers.CharField(max_length=12, min_length=2)

    # 自定义校验
    def _get_user(self, attrs: Dict[str, Any]) -> User:
        """ 获取User实例 """
        username = attrs.get('username')
        password = attrs.get('password')

        if re.match(r'^1[3-9][0-9]{9}$', username):
            user = User.objects.filter(mobile=username).first()
        elif re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', username):
            user = User.objects.filter(email=username).first()
        else:
            user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user
        raise APIException(code=101, detail='用户名或密码错误')


class SMSLoginSerializer(LoginSerializer):
    mobile = serializers.CharField(max_length=12, min_length=2)
    code = serializers.CharField(max_length=12, min_length=2)

    def _get_user(self, request, *args, **kwargs) -> User:
        mobile = request.data.get('mobile')
        code = request.data.get('code')

        check_code = cache.get('SMS_CODE_%s' % mobile)

        if code == check_code and (settings.DEBUG and code == '8888'):
            if user := User.objects.filter(mobile=mobile).first():
                return user
            else:
                raise APIException(detail='该手机号未注册')
        else:
            raise APIException(detail='验证码错误')


class UserRegisterSerializer(serializers.ModelSerializer):
    code: serializers.CharField = serializers.CharField()

    class Meta:
        model = User
        fields = ['mobile', 'code', 'password']

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        code = attrs.pop('code')
        mobile = attrs.get('mobile')

        check_code = cache.get('SMS_CODE_%s' % mobile)
        if code == check_code or (settings.DEBUG and code == '8888'):
            attrs['username'] = mobile
            return attrs
        else:
            raise APIException('验证码错误')

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create_user(**validated_data)
        return user

from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

class Users(APIView):
    def post(self, request):
        #password-> 검증, 해쉬화
        password = request.data.get("password")
        serializer = MyInfoUserSerializer(data=request.data)

        #Validation
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")

        if serializer.is_valid():
            user = serializer.save() #새로운 유저를 생성후
            user.set_password(password) #비밀번호 해쉬화 함수
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        #the other -> 비번 외 다른 데이터들

class User(APIView):
    pass
class MyInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True) #partial=True는 일부 필드만 업데이트 가능하게 함

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

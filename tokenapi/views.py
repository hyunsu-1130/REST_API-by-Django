from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets

class CustomAuthToken(ObtainAuthToken):   # 이미 있는 사용자에 대해서 토큰을 발급
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)   # 토큰 생성 or 가져오기
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

'''
# 만약 신규 사용자를 만들고 싶다면?  
class CreatUserView(viewsets.ModelViewSet):
    def post(self):
        pass
'''
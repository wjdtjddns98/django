from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from users.models import CustomUser

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth")  #JWT 토큰

        if not token:
            return None

        try:
            decoded = jwt.decode(token,
                       settings.SECRET_KEY,
                       algorithms=["HS256"])
            user_id = decoded.get('id')

            if not user_id:
                raise AuthenticationFailed("User not found")
            user = CustomUser.objects.get(id=user_id)

            return user


        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Invalid token")
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("User not found")


from firebase_admin import auth
from firebase_admin import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "").split()
        if len(auth_header) != 2 or auth_header[0].lower() != "bearer":
            return None

        token = auth_header[1]

        # try:
        #     decoded_token = auth.verify_id_token(token)
        #     return (decoded_token, None)
        # except Exception as e:
        #     raise AuthenticationFailed(str(e))

        try:
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token
            return (decoded_token, None)
        except ValueError as e:
            raise AuthenticationFailed(str(e))
        except exceptions.FirebaseError as e:
            raise AuthenticationFailed(str(e))

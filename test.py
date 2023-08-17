import jwt
from django.conf import settings


def ab():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMjM4Mzc2LCJpYXQiOjE2OTIyMzQ3NzYsImp0aSI6ImFmMTNlNzAyODRjNDQ1MDZiMmE5MjNiYmJhMjlhMGRiIiwidXNlcl9waG9uZV9udW1iZXIiOiIwMTA0OTQzNTE4NCJ9.oT7vvEUjvSMuHC9bhx2QOn0NBqE08LpCpfDTeycCJoU"

    decoded_token = jwt.decode(
        token, settings.SECRET_KEY, algorithms=["HS256"], options={"verify_exp": False}
    )

    issued_at = decoded_token["iat"]
    expiration_time = decoded_token["exp"]

    from datetime import datetime

    issued_at_datetime = datetime.fromtimestamp(issued_at)
    expiration_time_datetime = datetime.fromtimestamp(expiration_time)

    print(f"발급시간 : {issued_at_datetime}")
    print(f"만료시간 : {expiration_time_datetime}")

    now = datetime.now()
    time_left = expiration_time_datetime - now

    print(f"남은 시간 : {time_left}")

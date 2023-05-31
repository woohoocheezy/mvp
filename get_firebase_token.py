import firebase_admin
from firebase_admin import credentials, auth

# Initialize the Firebase Admin SDK with your service account credentials
cred = credentials.Certificate("spacebar-83b06-firebase-adminsdk-t48ml-5d47594f54.json")
firebase_admin.initialize_app(cred)

# Generate a new Firebase auth token for the desired user
user = auth.get_user_by_email("backend0@test.com")
firebase_token = auth.create_custom_token(user.uid)

# Get the string representation of the token to use in the "Authorization" header
auth_token = f"Bearer {firebase_token.decode()}"
print(auth_token)

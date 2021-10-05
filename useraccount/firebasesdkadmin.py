import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime



creds = credentials.Certificate("firebase-creds.json")

firebase_admin.initialize_app(creds, {
    'databaseURL': 'https://vue-chat-app-a0d64-default-rtdb.firebaseio.com/',
})

ref = db.reference('messeges')

message = ref.push({
    "message" : "Hello from Ateeq",
    "recieverId": 3,
    "room": "4_3",
    "sendBy": 4,
    "senderId": 4,
    "time": int(datetime.now().timestamp())
})
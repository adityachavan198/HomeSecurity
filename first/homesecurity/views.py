from django.shortcuts import render
from django.urls import reverse
from django.http import *
# Create your views here.
from library.models import Student
from library.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
import face_recognition
from django.core.files.storage import FileSystemStorage
from glob import glob
import os
from pusher_push_notifications import PushNotifications
from fcm_django.models import FCMDevice
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/adityachavan/Desktop/aditya/Web-Technologies-College/django/first/homesecurity/home-f9a5e-firebase-adminsdk-bcmh2-5af7dffa49.json")
firebase_admin.initialize_app(cred)
# Create your views here.
yo = glob('/Users/adityachavan/Desktop/aditya/Web-Technologies-College/django/first/unknown*')
if len(yo)>0:
    maxi=int(yo[-1][-6])
else:
    maxi = 0
# def givename():
#     global maxi
#     list=['unknown']*100
#     num=[i for i in range(100)]
#     for

def face_recog():
    files = glob('/Users/adityachavan/Desktop/aditya/Web-Technologies-College/django/first/face_db/*')
    for i in files:
        picture_of_me = face_recognition.load_image_file(i)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
        t = "unknown" + str(maxi) + ".jpeg"
        unknown_picture = face_recognition.load_image_file(t)

        face_encode = face_recognition.face_encodings(unknown_picture)
        if len(face_encode)>0:
            unknown_face_encoding = face_encode[0]
        else:
            return[False]
            # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        if results[0]==True:
            return [True,i[i.rindex('/')+1:]]
    else :                   # For else hai ye chomu
        return [False]
@csrf_exempt
def index(request):
    # for key, values in request.POST.lists():
    #      print(key, values)
    print(type(request.FILES['file']))
    myfile = request.FILES['file']
    fs = FileSystemStorage()
    global maxi
    maxi += 1
    filename = fs.save('unknown'+str(maxi)+'.jpeg', myfile)

    result = face_recog()
    # uploaded_file_url = fs.url(filename)
    # open("/Users/adityachavan/Desktop/abc.jpeg", 'w')
    # print(request.POST)
    # return render(request, 'homesecurity/index.html')

    if result[0] == True:
        push_notify(result[1].split('.')[0])
        return HttpResponse(json.dumps([True, result[1]]), content_type='application/json')
    else:
        push_notify('UnAuthorized User at Door please your mail.')
        return HttpResponse(json.dumps(["False"]), content_type='application/json')

def push_notify(name):
    beams_client = PushNotifications(instance_id='7621a68e-ca79-4b07-9c74-4089312879f5', secret_key='F4643550FE18BFFB40AAED1C88AF7028C5B25EB3DAB29771821D1B12F83B82BC',)
    response = beams_client.publish_to_interests(interests=['hello'], publish_body={'apns': {'aps': {'alert':'User Authenticated'}},
        'fcm': {
            'notification': {
                'title': str(name),
                'body': str(name) + ' is home!'
            }
        }
    }
)

def pushi_notify(name):


    devices = FCMDevice.objects.all()
    print(devices)
    # for i in devices:
    #     print(i)
    # print(name)

    print(devices.send_message(title="hello", body=str(name)))
    #devices.send_message(title="Title", body=str(name), data={"test": "test"})
    #devices.send_message(data={"test": "test"})

#mapping between url and view function to be called
from django.urls import path
from . import views
# module level variable n should be of that name only
urlpatterns=[
    path('',views.index, name='libraryindex'),
    path('aboutus/',views.aboutus),
    path('register/',views.register,name='libraryregister'),              # PASS ADDRESS OF FUNCTION
    path('students/', views.registerstudent, name='registerstudent'),
    path('auth/', views.authenticate, name='authenticateuser'),
    path('home/', views.showhome, name='showhomepage'),
    path('logout/', views.logout, name='logout')
]

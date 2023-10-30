from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homes,name="homes"),
    path('index',views.index,name='index'),
    path('login',views.login_view,name="login_view"),
    path('register',views.register,name="register"),
    path('candidate',views.candidate,name="candidate"),
    path('recruiter',views.recruiter,name="recruiter"),
    path('adminpage',views.admin,name="adminpage"),
    path('addjobs',views.addjobs,name="addjobs"),
    path('candidatehome',views.candidatehome,name="candidatehome"),
    path('candidatedetails',views.candidatedetails,name="candidatedetails"),
    path('candvid',views.candvid,name="call"),
    path('recvid',views.recvid,name="calls"),
    path('candidateinfo',views.candidateinfo,name="cdinfo"),
    path('mail',views.mail,name="mail"),
    path('resc',views.resources,name="resc"),
]

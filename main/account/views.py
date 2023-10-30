from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login
from .models import *
import smtplib
# Create your views here.

def candvid(request):
    return render(request,'candidatevideo.html')

def recvid(request):
    return render(request,'recruitervideo.html')

def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form, 'msg':msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_candidate:
                login(request,user)
                return redirect('candidate')
            elif user is not None and user.is_recruiter:
                return redirect('recruiter')

            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'login.html',{'form':form, 'msg' : msg})

def admin(request):
    return render(request,'admin.html')


def candidate(request):
    alljobs = Jobs.objects.all()
    context = {'candidate':alljobs}
    return render(request,'candidate.html',context)

def candidateinfo(request):
    allcands = Candidate.objects.all()
    context = {'candidates':allcands}
    return render(request,'candidateinfo.html',context)
    
def recruiter(request):
    return render(request,'recruiter.html')

def addjobs(request):
    if request.method == "POST":
        jobtitle = request.POST.get('jobtitle')
        companyname=request.POST.get('companyname')
        salary = request.POST.get('salary')
        experince = request.POST.get('experince')
        location = request.POST.get('location')
        opening = request.POST.get('opening')
        requirment = request.POST.get('requirment')
        job = Jobs(jobtitle=jobtitle,companyname=companyname,salary=salary,experince=experince,opening=opening,location=location,requirment=requirment)
        job.save()
    return render(request,'addjobs.html')


def candidatehome(request):
    
    return render(request,'candidatehome.html')

def candidatedetails(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        cand = Candidate(firstname=firstname,lastname=lastname,email=email,address=address,phone=phone,desc=desc)
        cand.save()
    return render(request,'candidatedetails.html',)

def homes(request):
    return render(request,'homes.html')



def mail(request):
    
#   server = smtplib.SMTP('smtp.gmail.com', 587)
#   server.ehlo()
#   server.starttls()
#   server.ehlo()
#   server.login('20131a1250@gvpce.ac.in', 'Vanamalz#7')
#   subject = request.POST.get('subject')
  
#      # massage = f"Subject : {subject}\n\n{body}"
#   message = 'Subject: {}\n\n{}'.format(subject, body)
#   server.sendmail(
#       '20131a1210@gvpce.ac.in',
#       'poornasai62@gmail.com',
#            message
#   )

#   print('Hey email has been sent!')
#   server.quit()
  return render(request,'mail.html')


def resources(request):
    return render(request,'resources.html')
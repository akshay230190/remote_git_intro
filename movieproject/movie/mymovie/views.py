
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from passlib.hash import sha256_crypt
from .models import Adduser
from django.views import View
from .movie import movie_popular,movie_rated,movie_drama,movie_action,movie_romance,movie_crime,movie_mystery,movie_sport




def index(request):
    #poplar list
    model=movie_popular(10)
    res=model.similarmovie()
    img,rating,name=[],[],[]
    for p in range(0,10):
        img.append(res[p][2])
        rating.append(res[p][0])
        name.append(res[p][1])
    #popular ends
    #rated start
    model_rated=movie_rated(10)
    res_rated=model_rated.similarmovie()
    img_rated,rating_rated,name_rated=[],[],[]
    for r in range(0,10):
        img_rated.append(res_rated[r][2])
        rating_rated.append(res_rated[r][0])
        name_rated.append(res_rated[r][1])
    #rated ends
    #drama begins
    model_d=movie_drama(10)
    res_d=model_d.similarmovie()
    img_d,rating_d,name_d=[],[],[]
    for d in range(0,10):
        img_d.append(res_d[d][2])
        rating_d.append(res_d[d][0])
        name_d.append(res_d[d][1])
    #drama ends
    #action begins
    model_a=movie_action(10)
    res_a=model_a.similarmovie()
    img_a,rating_a,name_a=[],[],[]
    for a in range(0,10):
        img_a.append(res_a[a][2])
        rating_a.append(res_a[a][0])
        name_a.append(res_a[a][1])
    #action ends
    #romance begins
    model_ro=movie_romance(10)
    res_ro=model_ro.similarmovie()
    img_ro,rating_ro,name_ro=[],[],[]
    for ro in range(0,10):
        img_ro.append(res_ro[ro][2])
        rating_ro.append(res_ro[ro][0])
        name_ro.append(res_ro[ro][1])
    #romance ends
    #crime begins
    model_c=movie_crime(10)
    res_c=model_c.similarmovie()
    img_c,rating_c,name_c=[],[],[]
    for c in range(0,10):
        img_c.append(res_c[c][2])
        rating_c.append(res_c[c][0])
        name_c.append(res_c[c][1])
    #crime ends
    #sports begins
    model_s=movie_sport(10)
    res_s=model_s.similarmovie()
    img_s,rating_s,name_s=[],[],[]
    for s in range(0,10):
        img_s.append(res_s[s][2])
        rating_s.append(res_s[s][0])
        name_s.append(res_s[s][1])
    #sports ends
    #mystery begins
    model_m=movie_mystery(10)
    res_m=model_m.similarmovie()
    img_m,rating_m,name_m=[],[],[]
    for m in range(0,10):
        img_m.append(res_m[m][2])
        rating_m.append(res_m[m][0])
        name_m.append(res_m[m][1])
    #action ends
    return render(request,"index.html",{'rating':rating,'name':name,'img':img,
                                        'rating_rated':rating_rated,'name_rated':name_rated,'img_rated':img_rated,
                                        'rating_d':rating_d,'name_d':name_d,'img_d':img_d,
                                        'rating_a':rating_a,'name_a':name_a,'img_a':img_a,
                                        'rating_ro':rating_ro,'name_ro':name_ro,'img_ro':img_ro,
                                        'rating_c':rating_c,'name_c':name_c,'img_c':img_c,
                                        'rating_s':rating_s,'name_s':name_s,'img_s':img_s,
                                        'rating_m':rating_m,'name_m':name_m,'img_m':img_m
                                        })
    #return HttpResponse(name)
    
    #return render(request,"index.html")

def aftersignup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        repass=request.POST.get("repassword")
        if password==repass:
            request.session['username']=username
            request.session['email']=email
            request.session['password']=password
            subject="Email for validation"
            otp=randint(1000,9999)
            request.session['otp']=otp
            message=f"Please enter otp for validation {otp} "
            from_email="batwara.akshay0@gmail.com"
            to_email=email
            try:
                send_mail(subject,message,from_email,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
                #return HttpResponse("mail send")
            except Exception as e:
                return HttpResponse(e)
                return render(request,"index.html")
            else:
                
                return render(request,"index.html",)
                
        return HttpResponse("error")
def afterverify(request):
    userotp=request.POST.get("userotp")
    #return HttpResponse(request.session["otp"])
    if userotp==str(request.session.get('otp')):
        del request.session["otp"]
        #return HttpResponse("otp matched")
        try:
            Adduser.objects.get(email=str(request.session['email']))
        except:
            password=sha256_crypt.hash(str(request.session.get('password')))
            #return HttpResponse(str(request.session.get('username')))
            Adduser.objects.create(fullname=str(request.session.get('username')),email=str(request.session.get("email")),password=password)
            del request.session["username"]
            del request.session["email"]
            del request.session["password"]
            return render(request,"index.html")
        else:
            return HttpResponse("not saved in database")

    else:
        return HttpResponse("otp not match")
def viewall(request):
    return render(request,"viewall.html")
    # Create your views here.

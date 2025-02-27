from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from app.models import Company
from app.models import profile_image
from app.models import College_User
from app.models import College_Events
from app.models import Contact




from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse


def home(request):
        if 'submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            contact = Contact(name=name, email=email, phone=phone, message=message)
            # contact.save()
            print(name,email,phone,message)
            contact.save()
            messages.success(request, "Thanks for Reaching Us! We will get back to you soon....")
        return render(request, 'home.html')

# def college_events(request):
#     return render(request, 'college_events.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpass = request.POST.get('conpass')
        print(username,firstname,lastname,email,password,conpass)
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email already exists')
            return redirect('/signup/')
        elif password != conpass:
            messages.warning(request,'invalid username or password')
        else:
            user = User(username=username,first_name=firstname,last_name=lastname,email=email)
            user.set_password(password)
            user.save()
            messages.success(request, "details Added Successfully")
            return redirect('/login/')
    return render(request,'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('/login/')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('/home/')

def profile(request,id):
    uid=request.user.id
    college_user = 0
    user = User.objects.get(id=id)
    count = College_User.objects.filter(uid_id = uid).exists()
    if College_User.objects.filter(uid_id = uid).exists():
        college_user = College_User.objects.get(uid_id = uid)
    # print(college_user)
    count_c = Company.objects.filter(uid_id = uid).exists()
    # print(count)
    if profile_image.objects.filter(user_id=uid).exists():
            pro=profile_image.objects.get(user_id=uid)
            image=pro.image
    else:
        image=False
    if 'image' in request.FILES:
        image = request.FILES['image']
    elif image is None:
        image= profile_image.objects.get(image=image)
        print(image)
    user1 = profile_image(user_id= uid,image = image)
    if 'editpro' in request.POST:
        user1.save() 
        url = '/home/profile/'+str(uid)
        return redirect(url)
    return render(request,'profile.html',{'users':user,'user1':user1,'count1': count,'count2':count_c,'collegeuser' : college_user})



def college_details(request):
    if request.method == 'POST':
        uid = request.user.id
        college_name = request.POST.get('name')
        college_email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        image = request.FILES['image']
        print(college_name,college_email,number)
        if College_User.objects.filter(email=college_email).exists():
            messages.warning(request,'details already exists')
        else:
            collegeuser = College_User(name=college_name,address=address,email=college_email,college_contact=number,image=image,uid_id=uid)
            collegeuser.save()
            messages.success(request, "details Added Successfully")
            # return redirect('/profile/')
            url = '/home/profile/'+str(uid)
            return redirect(url)
    return render(request, 'college_user.html')


def colleges(request):
    colleges = College_User.objects.all()
    print(colleges)
    return render(request, 'colleges.html', {'college': colleges})

    

def company_details(request):
    if request.method == "POST":
        uid = request.user.id
        name = request.POST.get('name')
        details = request.POST.get('details')
        email = request.POST.get('email')
        number = request.POST.get('number')
        image = request.FILES['image']
        address = request.POST.get('address')
        count = Company.objects.filter(uid_id = uid).exists()
        if Company.objects.filter(company_name=name).exists():
            messages.warning(request,'company already exists')
        else:
            company = Company(company_name=name,company_details =details,company_number=number,company_email=email,company_image=image,company_address=address,uid_id = uid)
            company.save()
            messages.success(request, "details Added Successfully")
            url = '/home/profile/'+str(uid)
            return redirect(url)
    return render(request, 'company_details.html')


def companies(request):
    companies = Company.objects.all()
    print(companies)
    return render(request, 'companies.html', {'company': companies})


def college_event_details(request,id):
    # uid = request.user.id
    # if College_User.objects.filter(uid_id = uid).filter(id=id).exists():
    #     college_id = College_User.objects.values('id').get(id=id)
    #     print(college_id)
    if request.method == "POST":
        name = request.POST.get('name')
        schedule = request.POST.get('schedule')
        type = request.POST.get('type')
        description = request.POST.get('description')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        if College_Events.objects.filter(name=name).exists():
            messages.warning(request,'event already exists')
        else:
            events = College_Events(name=name,schedule=schedule,description=description,eventType=type,image1=image1,image2=image2,image3=image3,cid_id =id)
            events.save()
            messages.success(request, "event details Added Successfully")
        url = '/home/profile/'+str(request.user.id)
        return redirect(url)
    return render(request, 'college_Event_Details.html')


def college_events(request,id):
    college_events=College_Events.objects.filter(cid_id=id)
    if request.user.id == College_User.uid_id:
        cid = College_User.objects.values('id').get(uid_id = request.user.id)
        clgid = cid.get('id')
        print(cid,clgid,id)
        return render(request,'college_events.html',{'college_events1':college_events,'cid1':clgid})
    else:   
        return render(request,'college_events.html',{'college_events1':college_events})


def edit_event_details(request,name,id):
    college_events = College_Events.objects.get(id=name,cid_id=id)
    colleges = College_User.objects.get(id=id)
    if request.method=='POST' and 'image1' in request.FILES and 'image2' in request.FILES and 'image3' in request.FILES:
        name1 = request.POST.get('name')
        type =request.POST.get('type')
        schedule =request.POST.get('schedule')
        description =request.POST.get('description')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        college_events.name = name1
        college_events.eventType = type
        college_events.schedule = schedule
        college_events.description = description
        college_events.image1 = image1
        college_events.image2 = image2
        college_events.image3 = image3
        college_events.save()
        return redirect('/home/')
    print(college_events)

    return render(request, 'edit_event_details.html',{'college_events1':college_events,'colleges1':colleges})

        
           
      


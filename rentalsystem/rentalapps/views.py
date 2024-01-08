from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from .models import customusers
from .models import Car,customusers
from .models import Booking
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        location = request.POST['location']
        company_name = request.POST['company_name']
        user = customusers.objects.create_user(username=username,first_name=first_name,last_name=last_name,user_type=0,email=email,address=address,company_name=company_name,
                                              phone=phone,password=password,location=location)
        user.save()
        # return redirect()
        return HttpResponse('create')
    else:
        return render(request, 'user/register.html')


def company_register(request):
    if request.method == 'POST':
        company_name = request.POST['companyname']
        username = request.POST['username']
        company_address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        location = request.POST['location']
        password = request.POST['password']
        data = customusers.objects.create_user(company_name=company_name,address=company_address,location=location,user_type=1,phone=phone,username=username,
                                               email=email,password=password)
        data.save()
        return HttpResponse("company register successful")
    else:

        return render(request,'company/branch.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin:index')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 1:# company has logined
                return redirect(user_page)
            elif user.user_type == 0:# coutsomuser has has logined
                return redirect(userindex)
        else:
            return render(request, 'login.html',)

    return render(request, 'login.html')  # Render the login page for GET requests


def add_car(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        name = request.POST['name']
        car_model = request.POST['car_model']
        price = request.POST['price']
        image = request.FILES['image']
        details = request.POST['details']
        new_car = Car.objects.create(company_id=user,name=name, car_model=car_model, price=price, details=details,image=image)
        new_car.save()
        # return HttpResponse('Car added successfully')
        return redirect(view_car)
    else:
        return render(request, 'company/addcar.html',)

def view_car(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    return render(request, 'company/carview.html', {'data': data})


def view_users(request):
    data = customusers.objects.get(id=request.user.id)
    print(data.first_name)
    return render(request, 'company/userview.html', {'data': data})


def delete(request,id):
    user = customusers.objects.get(id=request.user.id)
    user = Car.objects.filter(id=id)

    user.delete()
    return redirect(view_car)


def edit_car(request,id):
    user = customusers.objects.get(id=request.user.id)
    datas = Car.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        car_model = request.POST['car_model']
        price = request.POST['price']
        details = request.POST['details']
        data = Car.objects.update(name=name, car_model=car_model,price=price,details=details)
        return redirect(view_car)
    else:
        return render(request,'company/edit.html',{'data':datas})


def update_company(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        company_name = request.POST['company_name']
        address = request.POST['company_address']
        location = request.POST['location']
        data = customusers.objects.update(company_name=company_name,
            address=address,
            location=location
    )
        return HttpResponse('Update successful')
    else:

        return render(request, '/company/update.html')



def car_request(request):
    user = customusers.objects.get(id=request.user.id)

    if request.method == 'POST':
        car_name = request.POST['name']
        details = request.POST['details']
        price = request.POST['price']
        car_request = Car.objects.create(name=car_name,details=details,price=price)
        return HttpResponse('Car request successfully added')
    else:
        return render(request, 'company/request.html',{'user':user})









def booking(requset):
    if requset.method == 'POST':
        user = requset.POST['user']
        no_of_days = requset.POST['no_of_days']
        day = requset.POST['day']
        Total_cost = requset.POST['Total_cost']
        booking_date = requset.POST[' booking_date']
        status = requset.POST['status']
        Bookings = Booking.objects.create(user=user,no_of_days=no_of_days,day=day,Total_cost=Total_cost,booking_date=booking_date,status='pending')

        Bookings.save()
        return HttpResponse('Booking successful')
    else:
        return render(requset, 'company/booking.html')





def company_review(request):
    data = customusers.objects.filter()
    return render(request, 'user/company_history.html',{'data':data})



def profile(request):
    data = customusers.objects.get()
    return render(request, 'profile.html', {'data': data})


def car_request(request,id):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        no_of_days = int(request.POST['no_of_day'])
        day = request.POST['day']
        booking_date = request.POST['booking_date']


        car = Car.objects.get(id=id)
        cost = no_of_days * car.daily_rate
        car.Total_cost += cost
        car.save()
        booking_request = Booking.objects.create(
            user=user,
            car=car,
            no_of_days=no_of_days,
            day=day,
            booking_date=booking_date
        )
        booking_request.save()
        return HttpResponse('Car request successfully added')
    else:
        return render(request, 'company/request.html', {'user': user})


# def car_request(request):
#     user = Car.objects.get(id=request.user.id)
#
#     if request.method == 'POST':
#         car_name = request.POST['car']
#         no_of_day = request.POST['no_of_day']
#         day = request.POST['data']
#         Total_cost = request.POST['Total_cost']
#         booking_date = request.POST['booking_data']
#         car_request = Booking.objects.create(name=car_name,no_of_day=no_of_day,day=
#                                              day,Total_cost=Total_cost,booking_date=booking_date)
#         if user > 100:
#             amount = addcash + bank.amount
#             bank.amount = amount
#             bank.save()
#         car_request.save()
#         return HttpResponse('Car request successfully added')
#     else:
#         return render(request, 'company/request.html',{'user':user})







# def search(request) :
#     if request.user.is_authenticated:
#         datas = Car.objects.filter(user = request.user)
#     searchs = customusers.objects.get(id=request.user.id)
#     return render (request,'search.html')

def user_history(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    data = customusers.objects.all()
    return render(request, 'company/user/user_history.html',{'datta':data})

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect(userindex)

def companylogout(request):
    auth.logout(request)
    return redirect(cmpnyindex)

def abouts(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contact.html')
def cmpnyindex(request):
    return render(request, 'company/companyindex.html')

def userindex(request):
    return render(request, 'user/userindex.html')
def services(request):

    return render(request, 'service.html')
def user_page(request):
    return render(request, 'company/companyindex.html')
def cars(request):
    return render(request, 'car.html')


def details(request):
    return render(request, 'detail.html')

def bookings(request):
    return render(request, 'company/booking.html')
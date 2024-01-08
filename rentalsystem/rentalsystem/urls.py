"""
URL configuration for carrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rentalapps import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_register',views.user_register, name='user_register'),
    path('user_login',views.user_login, name='user_login'),
    path('company_register',views.company_register, name='company_register'),
    path('add_car',views.add_car, name='add_car'),
    path('',views.index,name="indexs"),
    path('cmpnyindex',views.cmpnyindex, name='cmpnyindex'),
    path('userindex',views.userindex, name="userindex"),
    path('services',views.services, name='service'),
    path('user_page',views.user_page, name='user_page'),
    path('cars',views.cars, name='cars'),
    path('details',views.details, name='details'),
    path('contacts',views.contacts, name='contacts'),
    path('booking',views.booking, name='booking'),
    path('abouts',views.abouts, name='abouts'),
    path('update_company',views.update_company, name='update_company'),
    path('logout',views.logout, name='logout'),
    path('companylogout',views.companylogout, name='companylogout'),
    path('view_users',views.view_users, name='view_users'),
    path('car_request',views.car_request, name='car_request'),
    # path('profile',views.profile),
    path('edit_car/<int:id>',views.edit_car, name="edit_car"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('view_car',views.view_car, name="view_car"),
    # path('search',views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Truck,Notification
import datetime
# Create your views here.


#def home_page(request):


def truck_page(request):    
    read=[]
    unread=[]
    def check_expiry_date(self):
        trucks = Truck.objects.all()
        for truck in trucks:
            insurance=truck.insurance_number
            fitness=truck.fitness_certificate_id
            insurance_expiry_date = truck.insurance_expiry
            fitness_expiry_date = truck.fitness_certificate_expiry
            check_date1 = int((insurance_expiry_date - datetime.date.today()).days)
            check_date2=int((fitness_expiry_date - datetime.date.today()).days)
            print (check_date1)
            print (check_date2)
            global i
            if check_date1== 7 or check_date1== 15 or check_date1== 30:
                obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Insurance-id-"+str(insurance),days_remaining=check_date1)
                if notif is True:
                    obj.save()
            if check_date2== 7 or check_date2== 15 or check_date2== 30:
                obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Fitness-id-"+fitness,days_remaining=check_date2)
                if notif is True:
                    obj.save()
    check_expiry_date(request)
    return render(request,"companies/trucks.html",{'x':1,'y':Notification.objects.all,'trucks':Truck.objects.all})

def mark_read(request):
    notifications=Notification.objects.all()
    for notif in notifications:
        licence=notif.licence_type
        if notif.is_read is False:
            t=Notification.objects.get(licence_type=licence)
            t.is_read=True
            t.save()
    return redirect("/")
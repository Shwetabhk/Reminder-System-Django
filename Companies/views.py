from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Truck,Notification
import datetime
# Create your views here.


#def home_page(request):


def truck_page(request):    
    read=[]
    unread=[]
    nots=Notification.objects.all()
    for i in nots:
        if i.is_read is True:
            read.append(i)
        else:
            unread.append(i)
    def check_expiry_date(self):
        trucks = Truck.objects.all()
        
        for truck in trucks:
            number=truck.truck_number
            insurance=truck.insurance_number
            fitness=truck.fitness_certificate_id
            insurance_expiry_date = truck.insurance_expiry
            fitness_expiry_date = truck.fitness_certificate_expiry
            check_date1 = int((insurance_expiry_date - datetime.date.today()).days)
            check_date2=int((fitness_expiry_date - datetime.date.today()).days)
            if check_date1== 7 or check_date1== 15 or check_date1== 30:
                obj,notif=Notification.objects.get_or_create(truck_id=truck.id,truck=number,company_name="Gurgaon",licence_type="Insurance-id-"+str(insurance),days_remaining=check_date1)
                if notif is True:
                    obj.save()
            if check_date2== 7 or check_date2== 15 or check_date2== 30:
                obj,notif=Notification.objects.get_or_create(truck_id=truck.id,truck=number,company_name="Gurgaon",licence_type="Fitness-id-"+fitness,days_remaining=check_date2)
                if notif is True:
                    obj.save()
    check_expiry_date(request)
    return render(request,"companies/trucks.html",{'x':1,'y':Notification.objects.all,'trucks':Truck.objects.all,'read':len(read),'unread':len(unread)})

def mark_read(request):
    notifications=Notification.objects.all()
    for notif in notifications:
        licence=notif.licence_type
        if notif.is_read is False:
            t=Notification.objects.get(licence_type=licence)
            t.is_read=True
            t.save()
    return redirect("/")


def truck_detail(request,pk=None,*args,**kwargs):
    read=[]
    unread=[]
    nots=Notification.objects.all()
    for i in nots:
        if i.is_read is True:
            read.append(i)
        else:
            unread.append(i)
    trucks = Truck.objects.all()
    for truck in trucks:
        insurance=truck.insurance_number
        fitness=truck.fitness_certificate_id
        insurance_expiry_date = truck.insurance_expiry
        fitness_expiry_date = truck.fitness_certificate_expiry
        check_date1 = int((insurance_expiry_date - datetime.date.today()).days)
        check_date2=int((fitness_expiry_date - datetime.date.today()).days)
        global i
        if check_date1== 7 or check_date1== 15 or check_date1== 30:
            obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Insurance-id-"+str(insurance),days_remaining=check_date1)
            if notif is True:
                obj.save()
        if check_date2== 7 or check_date2== 15 or check_date2== 30:
            obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Fitness-id-"+fitness,days_remaining=check_date2)
            if notif is True:
                obj.save()
    instance=get_object_or_404(Truck,pk=pk)
    context={
        "instance":instance,
        'x':1,
        'y':Notification.objects.all,
        'trucks':Truck.objects.all,
        'read':len(read),
        'unread':len(unread)
    }
    return render(request,"companies/detail.html",context)
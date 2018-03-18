from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Truck,Notification
import datetime
import csv
import os

#Function for Rendering the home page and checking the expiry date and generate notifications if not already created.
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


#Function for Mark as read feature in the notifications.
def mark_read(request):
    notifications=Notification.objects.all()
    for notif in notifications:
        licence=notif.licence_type
        if notif.is_read is False:
            t=Notification.objects.get(licence_type=licence)
            t.is_read=True
            t.save()
    return redirect("/")

#Corresponding details for each truck and the same function for notifications.
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
        if check_date1== 7 or check_date1== 15 or check_date1== 30:
            obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Insurance-id-"+str(insurance),days_remaining=check_date1)
            if notif is True:
                obj.save()
        if check_date2== 7 or check_date2== 15 or check_date2== 30:
            obj,notif=Notification.objects.get_or_create(company_name="Gurgaon",licence_type="Fitness-id-"+fitness,days_remaining=check_date2)
            if notif is True:
                obj.save()
    instance=get_object_or_404(Truck,pk=pk) # Using Primary Key for id.
    context={
        "instance":instance,
        'x':1,
        'y':Notification.objects.all,
        'trucks':Truck.objects.all,
        'read':len(read),
        'unread':len(unread)
    }
    return render(request,"companies/detail.html",context)
def tabular_detail(request):
    context={
        'trucks':Truck.objects.all       
    }
    return render(request,"companies/tabular.html",context)


def tabular_upload(request):
    context={
        'trucks':Truck.objects.all       
    }
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(THIS_FOLDER, 'truck.csv')
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Truck.objects.get_or_create(
                id=row[0],
                truck_number=row[1],
                insurance_number=row[2],
                insurance_expiry=row[3],
                fitness_certificate_expiry=row[4],
                fitness_certificate_id=row[5],
                image=row[6],
                ) 

    return render(request,"companies/tabular.html",context)
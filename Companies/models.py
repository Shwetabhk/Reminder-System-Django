from django.db import models
import random
import os
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _

class Company(models.Model):
    name=models.CharField(max_length=80)
    def __str__(self):
        return self.name


def get_file_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename=str(random.randint(0,1000000))
    name,ext=get_file_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "trucks/truck{final_filename}".format(final_filename=final_filename)


class Truck(models.Model):
    company=models.ForeignKey(Company)
    truck_number=models.CharField(max_length=14)
    insurance_number=models.PositiveIntegerField()
    insurance_expiry=models.DateField()
    fitness_certificate_id=models.CharField(max_length=30,null=True,blank=True)
    fitness_certificate_expiry=models.DateField(null=True,blank=True)
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True)

    def __str__(self):
        return self.company.name+"-"+self.truck_number


class Notification(models.Model):
    serial=models.PositiveIntegerField()
    company_name=models.CharField(max_length=80)
    licence_type = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    days_remaining=models.PositiveIntegerField()
    is_read = models.BooleanField(_('Is read?'), default=False)

    def __str__(self):
        title = _('%(serial)s . %(company)s licence %(licence)s will expire in %(days)s days')
        return title % {'serial':self.serial,'company': self.company_name, 'licence': self.licence_type,
                        'days':self.days_remaining}

    class Meta:
        verbose_name_plural = _('notifications')
        ordering = ['-created']

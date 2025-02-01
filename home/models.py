# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    tax_id = models.TextField(max_length=255, null=True, blank=True)
    obs = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Acts_Type(models.Model):

    #__Acts_Type_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    #__Acts_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Acts_Type")
        verbose_name_plural = _("Acts_Type")


class Acts(models.Model):

    #__Acts_FIELDS__
    acts_type_id = models.ForeignKey(acts_type, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)

    #__Acts_FIELDS__END

    class Meta:
        verbose_name        = _("Acts")
        verbose_name_plural = _("Acts")


class Acts_Logs(models.Model):

    #__Acts_Logs_FIELDS__
    acts = models.ForeignKey(acts, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    pacient_name = models.TextField(max_length=255, null=True, blank=True)

    #__Acts_Logs_FIELDS__END

    class Meta:
        verbose_name        = _("Acts_Logs")
        verbose_name_plural = _("Acts_Logs")


class Invoices(models.Model):

    #__Invoices_FIELDS__
    invoice_number = models.TextField(max_length=255, null=True, blank=True)
    number_lines = models.IntegerField(null=True, blank=True)
    total_value = models.IntegerField(null=True, blank=True)

    #__Invoices_FIELDS__END

    class Meta:
        verbose_name        = _("Invoices")
        verbose_name_plural = _("Invoices")


class Invoice_Lines(models.Model):

    #__Invoice_Lines_FIELDS__
    invoice_id = models.ForeignKey(invoices, on_delete=models.CASCADE)
    invoice_description = models.TextField(max_length=255, null=True, blank=True)
    invoice_data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    invoice_value = models.IntegerField(null=True, blank=True)

    #__Invoice_Lines_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice_Lines")
        verbose_name_plural = _("Invoice_Lines")


class Acts_Invoices(models.Model):

    #__Acts_Invoices_FIELDS__
    acts_id = models.ForeignKey(acts, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(invoice_lines, on_delete=models.CASCADE)

    #__Acts_Invoices_FIELDS__END

    class Meta:
        verbose_name        = _("Acts_Invoices")
        verbose_name_plural = _("Acts_Invoices")



#__MODELS__END

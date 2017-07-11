from __future__ import unicode_literals

from django.db import models

#clientes
class Customer(models.Model):
    businessId = models.AutoField(primary_key=False)
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    additionalInfo = models.TextField()

#articulos
class Item(models.Model):
    businessId = models.AutoField(primary_key=False)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    specifications = models.CharField(max_length=500)
    manufacturingUrl = models.URLField(max_length=200)
    driversUrl = models.URLField(max_length=200)
    additionalInfo = models.TextField()
    owner = models.ManyToManyField(customer)

#ficha tecnica
class DataSheet(models.Model):
    businessId = models.AutoField(primary_key=False)
    description = models.CharField(max_length=200)
    tasks = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    status = models.ForeignKey(IssueStatus)
    operator = models.ForeignKey(Operator)
    dataSheet = models.ForeignKey(DataSheet)
    startDate = models.DateTimeField('Fecha de Inicio')
    endDate = models.DateTimeField('Fecha de Finalizacion')

class DataSheetStatus(models.Model):
    businessId = models.AutoField(primary_key=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

#Incidencia
class Issue(models.Model):
    businessId = models.AutoField(primary_key=False)
    description = models.CharField(max_length=200)
    tasks = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    status = models.ForeignKey(IssueStatus)
    operator = models.ForeignKey(Operator)
    dataSheet = models.ForeignKey(DataSheet)
    startDate = models.DateTimeField('Fecha de Inicio')
    endDate = models.DateTimeField('Fecha de Finalizacion')

class IssueStatus(models.Model):
    businessId = models.AutoField(primary_key=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

#Tecnico
class operator(models.Model):
    businessId = models.AutoField(primary_key=False)
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    additionalInfo = models.TextField()



from __future__ import unicode_literals

from django.db import models

#clientes
class Customer(models.Model):
    businessId = models.IntegerField()
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    additionalInfo = models.TextField()

    def save(self):
        top = Customer.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(Customer, self).save()


#Tecnico
class Operator(models.Model):
    businessId = models.IntegerField()
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    additionalInfo = models.TextField()

    def save(self):
        top = Operator.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(Operator, self).save()


#articulos
class Item(models.Model):
    businessId = models.IntegerField()
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    specifications = models.CharField(max_length=500)
    manufacturingUrl = models.URLField(max_length=200)
    driversUrl = models.URLField(max_length=200)
    additionalInfo = models.TextField()
    owner = models.ManyToManyField(Customer, through='ItemInstance')

    def save(self):
        top = Item.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(Item, self).save()


class ItemInstance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    serialNumber = models.CharField(max_length=200)
    additionalInfo = models.TextField()


class DataSheetStatus(models.Model):
    businessId = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def save(self):
        top = DataSheetStatus.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(DataSheetStatus, self).save()


#ficha tecnica
class DataSheet(models.Model):
    businessId = models.IntegerField()
    description = models.CharField(max_length=200)
    tasks = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    status = models.ForeignKey(DataSheetStatus, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    startDate = models.DateTimeField('Fecha de Inicio')
    endDate = models.DateTimeField('Fecha de Finalizacion')

    def save(self):
        top = DataSheet.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(DataSheet, self).save()


class IssueStatus(models.Model):
    businessId = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def save(self):
        top = IssueStatus.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(IssueStatus, self).save()


#Incidencia
class Issue(models.Model):
    businessId = models.IntegerField()
    description = models.CharField(max_length=200)
    tasks = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    status = models.ForeignKey(IssueStatus, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    dataSheet = models.ForeignKey(DataSheet, on_delete=models.CASCADE)
    startDate = models.DateTimeField('Fecha de Inicio')
    endDate = models.DateTimeField('Fecha de Finalizacion')

    def save(self):
        top = Issue.objects.order_by('-businessId')[0]
        self.businessId = top.businessId + 1
        super(Issue, self).save()

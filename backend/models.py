from django.db import models

# Create your models here.
class Client(models.Model):
    clientid = models.AutoField(primary_key=True)
    clientcode = models.IntegerField()
    clientname = models.CharField(max_length=100)
    clienttype = models.CharField(max_length=100)


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    email = models.EmailField()
    officephone = models.IntegerField()
    cellphone = models.IntegerField()


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=30)
    phonenumber = models.IntegerField()


class TestStandard(models.Model):
    standardid = models.AutoField(primary_key=True)
    standardname = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publisheddate = models.DateField()


class Service(models.Model):
    serviceid = models.AutoField(primary_key=True)
    servicename = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    isfirequired = models.CharField(max_length=30)
    fifrequency = models.CharField(max_length=100)
    teststandardid = models.ForeignKey(TestStandard, on_delete=models.CASCADE)


class TestSequence(models.Model):
    sequenceid = models.AutoField(primary_key=True)
    sequencename = models.CharField(max_length=100)


class PerformanceData(models.Model):
    modelnum = models.IntegerField()
    testsequence = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    maxsysvoltage = models.IntegerField()
    voc = models.IntegerField()
    ics = models.IntegerField()
    vmp = models.IntegerField()
    imp = models.IntegerField()
    pmp = models.IntegerField()
    ff = models.IntegerField()


class Product(models.Model):
    modelnumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cell_technology = models.CharField(max_length=30)
    cellmanufacturer = models.CharField(max_length=30)
    numofcell = models.IntegerField()
    numofsellinseriece = models.IntegerField()
    numofseries = models.IntegerField()
    numofdiods = models.IntegerField()
    productlength = models.IntegerField()
    productwidth = models.IntegerField()


class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    certnumber = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    reportnumber = models.IntegerField()
    contactid = models.IntegerField()
    teststandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cert_issue_date = models.CharField(max_length=30)

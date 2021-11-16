from rest_framework import serializers
from ..models import Certificate
from ..models import Service
from ..models import Product
class CertificateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Certificate
        fields = ['id', 'certnumber', 'reportnumber','contactid','cert_issue_date']
     
class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['serviceid', 'servicename', 'description','isfirequired', 'fifrequency']
        
class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = ['modelnumber', 'name', 'cell_technology','cellmanufacturer', 'numofcell','numofsellinseriece',
                  'numofseries','numofdiods','productlength', 'productwidth']
   
 
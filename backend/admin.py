from django.contrib import admin

from backend.models import Certificate, Client, Location, Product, TestStandard, User

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(TestStandard)
admin.site.register(Certificate)

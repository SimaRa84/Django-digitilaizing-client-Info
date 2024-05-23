from django.contrib import admin

# Register your models here.
from .models import Customer, AccountInfo, CustomerDetails

class CustomerAdmin(admin.ModelAdmin):
    pass

class AccountInfoAdmin(admin.ModelAdmin):
    pass

class CustomerDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(AccountInfo, AccountInfoAdmin)
admin.site.register(CustomerDetails, CustomerDetailsAdmin)

from django.contrib import admin
from auth_app.models import Rider,Customer,RiderType,User

class RiderAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Rider, RiderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Customer, CustomerAdmin)
class RiderTypeAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(RiderType, RiderTypeAdmin)
class UserAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(User, UserAdmin)
from django.contrib import admin

# from .models import Company

# Register your models here.
# admin.site.register(Company)

from .models import Company, College_Events, College_User, Contact


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_details','uid', )
    search_fields = ('company_name',)
    list_filter=('company_name',)

class College_EventsAdmin(admin.ModelAdmin):
    list_display=('name', 'schedule','eventType','description',)
    search_fields = ('name', 'eventType',)
    list_filter = ( 'eventType', )
    list_per_page = 2

class College_UserAdmin(admin.ModelAdmin):
    list_display=('name', 'address',)
    search_fields = ('name', 'address',)
    list_filter = ('name', 'address', )

class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email',)
    


admin.site.register(Company, CompanyAdmin)
admin.site.register(College_Events,College_EventsAdmin)
admin.site.register(College_User,College_UserAdmin)
admin.site.register(Contact,ContactAdmin)

from django.contrib import admin
from .models  import Products,Order
# Register your models here.


admin.site.site_header = "E-commerce Site Maleme"
admin.site.site_title = "Malem Shopping"
admin.site.index_title = "Manage Maleme Shopping "

class  ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description='Defaulf Category'    
    list_display = ('title','price','discount_price','category','description')
    search_fields =('description',)
    actions =('change_category_to_default',)
    fields = ('title','price',)
    list_editable = ('price','category',)
    

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
from django.contrib import admin
from .models import Product , Offer

#this class defins how the product table should look like
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

#display the product class details to admin page
admin.site.register(Product,ProductAdmin)

#this class defins how the Offer table should look like
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount','description')

#display the offer class details to admin page
admin.site.register(Offer,OfferAdmin)

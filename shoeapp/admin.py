from django.contrib import admin
from . models import *
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_link','size','quantity']
    def product_link(self, obj):
        product = obj.product
        link = reverse("admin:shoeapp_product_change", args=[product.pk])  # Replace 'myapp' with your app name
        return format_html('<a href="{}">{}</a>', link, product.title)
    

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customers','products','quantity','size','ordered_date','status','payments']
    def customers(self,obj):
        link = reverse('admin:shoeapp_customer_change',args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)

    def products(self,obj):
        link = reverse('admin:shoeapp_product_change',args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    def payments(self,obj):
        link = reverse('admin:shoeapp_payment_change',args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>',link,obj.payment.razorpay_payment_id)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_link']
    def product_link(self, obj):
        product = obj.product
        link = reverse("admin:shoeapp_product_change", args=[product.pk])  # Replace 'myapp' with your app name
        return format_html('<a href="{}">{}</a>', link, product.title)

    product_link.short_description = 'Product'


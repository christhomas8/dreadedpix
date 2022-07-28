from django.contrib import admin
from .models import Gallery,Profile,Header,Bio,Inquiry

# Register your models here.

class imageAdmin(admin.ModelAdmin):
    list_display = ["image_tag","photo"]

class profileAdmin(admin.ModelAdmin):
    list_display = ["image_tag_1","avatarpic"]

class headerAdmin(admin.ModelAdmin):
    list_display = ["image_tag_2","headerpic"]

class inquiryAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","date"]


admin.site.register(Gallery, imageAdmin)
admin.site.register(Profile,profileAdmin)
admin.site.register(Header,headerAdmin)
admin.site.register(Bio)
admin.site.register(Inquiry,inquiryAdmin)

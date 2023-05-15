from django.contrib import admin
from .models import Book,Clothes,Miscellaneous,BookReq,MiscReq,ClothesReq
# Register your models here.

admin.site.register(Book)
admin.site.register(Clothes)
admin.site.register(Miscellaneous)
admin.site.register(BookReq)
admin.site.register(MiscReq)
admin.site.register(ClothesReq)
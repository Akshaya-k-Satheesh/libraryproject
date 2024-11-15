from django.contrib import admin
# Register your models here.


from users.models import CustomUser,Users

admin.site.register(CustomUser)

admin.site.register(Users)


from django.contrib import admin



# Register your models here.

from .models import Rate,History

admin.site.register(Rate)
admin.site.register(History)
from django.contrib import admin

# Register your models here.

from myapp.models import Pessoa

admin.site.register(Pessoa)

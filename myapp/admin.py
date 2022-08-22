from django.contrib import admin

# Register your models here.

from myapp.models import Pessoa,Aluno

admin.site.register(Pessoa)
admin.site.register(Aluno)
# No arquivo admin.py
from django.contrib import admin
from .models import Hemocentro, EstoqueSangue
from .forms import EstoqueSangueForm

class EstoqueSangueAdmin(admin.ModelAdmin):
    form = EstoqueSangueForm

admin.site.register(Hemocentro)
admin.site.register(EstoqueSangue, EstoqueSangueAdmin)

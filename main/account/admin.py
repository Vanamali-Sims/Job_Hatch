from django.contrib import admin
from .models import User,Jobs,Candidate
# Register your models here.
admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(Jobs)
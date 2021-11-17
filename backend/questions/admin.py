from django.contrib import admin
from .models import Answers, InputTypes, Question

admin.site.register(InputTypes)
admin.site.register(Question)
admin.site.register(Answers)

# Register your models here.

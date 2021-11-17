from django.contrib import admin
from .models import Answers, InputTypes, Options, Question, QuestionOptions

admin.site.register(InputTypes)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Options)
admin.site.register(QuestionOptions)

# Register your models here.

from django.contrib import admin
from .models import Patient, Comorbidity, KidneyStage, MealLog, FoodinMeal, Food, SerumLevelLog, SerumType

# Register your models here.
admin.site.register(Patient)
admin.site.register(Comorbidity)
admin.site.register(KidneyStage)
admin.site.register(MealLog)
admin.site.register(FoodinMeal)
admin.site.register(Food)
admin.site.register(SerumLevelLog)
admin.site.register(SerumType)
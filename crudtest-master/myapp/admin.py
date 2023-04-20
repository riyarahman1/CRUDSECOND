from django.contrib import admin

# Register your models here.
from myapp import models

admin.site.register(models.Project_Category)
admin.site.register(models.Project_Subcategory)
admin.site.register(models.Project)

from django.db import models

# Create your models here.
class Project_Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Project_Subcategory(models.Model):
    category = models.ForeignKey(Project_Category, on_delete = models.CASCADE)
    project_name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.project_name

class Project(models.Model):
    # projectcategory = models.ForeignKey(projectcategory, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(Project_Subcategory, on_delete=models.CASCADE)
    title =  models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


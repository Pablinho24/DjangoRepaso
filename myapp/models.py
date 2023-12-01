from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    #Muestra el nombre de los proyectos
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #También se puede concatenar con diferentes variables.
    def __str__(self):
        return self.title + ' - ' + self.project.name




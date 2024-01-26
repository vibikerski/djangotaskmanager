from django.db import models

class Status(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete = models.DO_NOTHING)
    creator = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title

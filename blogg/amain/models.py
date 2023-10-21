from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_created=True)
    content = models.TextField()

    def __str__(self):
        return str(self.date) + " " + self.title
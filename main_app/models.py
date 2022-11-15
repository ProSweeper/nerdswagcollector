from django.db import models

# Create your models here.
class Swag(models.Model):
  item = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.item}, item id: {self.id}'
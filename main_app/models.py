from django.db import models
from django.urls import reverse
from datetime import date, datetime, timedelta

# create a data structure for the cleaning methods
CLEANING = (
  ('D', 'Dust'),
  ('W', 'Wash'),
  ('P', 'Polish'),
)
# Create your models here.

class Set(models.Model):
  name = models.CharField(max_length=75)
  genre = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('sets_detail', kwargs={'pk': self.id})

class Swag(models.Model):
  item = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  # create the relationship between sets and swag (M:M)
  sets = models.ManyToManyField(Set)

  def __str__(self):
    return f'{self.item}, item id: {self.id}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'swag_id': self.id})

  def cleaned_this_week(self):
    today = date.today()
    week_ago = today - timedelta(days=7)
    return self.cleaning_set.filter(date__gt=week_ago).exists()
    

class Cleaning(models.Model):
  date = models.DateField('Cleaning Date')
  method = models.CharField(
    max_length=1,
    choices=CLEANING,
    default=CLEANING[0][0], 
  )
  # a cleaning belongs to an item so we need to create a foreign key for it
  swag = models.ForeignKey(
    # access the swag model
    Swag,
    # make sure that if we delete an item then it won't orphan any child attributes
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_method_display()}ed on {self.date}"
  
  # add a Meta class so we can change the ordering
  class Meta:
    ordering = ['-date']
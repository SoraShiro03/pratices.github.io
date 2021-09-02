from django.db import models
from django.forms import widgets
from django.urls import reverse
from django.utils import timezone

from taggit.managers import TaggableManager

class AnimeList(models.Model):
   name = models.CharField(max_length=255)
   slug = models.SlugField()
   description = models.TextField(blank=True)
   image = models.ImageField(upload_to='media/')
   date_posted = models.DateTimeField(default=timezone.now)

   tags = TaggableManager(blank=True)

   def get_absolute_url(self):
      
      return reverse("list_detail", args=[
         self.date_posted.year,
         self.date_posted.month,
         self.date_posted.day,
         self.slug
      ])
   
   def __str__(self):
      return self.name
   
   class Meta:
      ordering = ('-date_posted',)


   
from django.db import models
from django.db.models import fields
from .models import AnimeList
from django import forms

class AnimeListPostForm(forms.ModelForm):
   
   class Meta:
      model =  AnimeList
      fields = ('name', 'description', 'image')
from django.db import models

# Create your models here.
class Writings(models.Model):
  title = models.CharField(max_length=200)
  verse = models.CharField(max_length=30, null=True)
  bible_text = models.TextField(null=True)
  notes = models.TextField()
  pub_date = models.DateTimeField('date published', auto_now_add=True)
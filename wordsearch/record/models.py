from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Word(models.Model):
    word_text = models.CharField(max_length=100)
    word_num = models.IntegerField(default=0)
    def __str__(self):
        return self.word_text

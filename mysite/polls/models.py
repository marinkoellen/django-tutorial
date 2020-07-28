from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
#Question - name of table
#question_text = name of field
#models.Model inherit some information from this class
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        #if statement not needed, saying if publish date greater than timezone-1 day ago (more recent) then return true
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


#ForeignKey is saying its connected to another table
#so it is pointing it to other table
#cascade option - deletes all choices that are related to question if question deleted
class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
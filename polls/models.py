from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.choice_text}'


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
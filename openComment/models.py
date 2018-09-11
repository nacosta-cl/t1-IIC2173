from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment = models.CharField(max_length=2000)
    time = models.CharField(max_length=2000)


from django.forms import ModelForm
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment', 'time']



# Create your models here.

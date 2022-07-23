from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank = True)
    hashtags = models.ManyToManyField('Hashtag', blank = True, null = True, editable = True)

    def __str__(self):
        return self.title

class Comment(models.Model) :
    def __str__(self) :
        return self.text

    blog_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.CharField(max_length=50)

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
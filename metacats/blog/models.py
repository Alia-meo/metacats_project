from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Post', max_length=500)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date&Time')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='article', blank=True, null=True,
                                related_name='comments_articles')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user', blank=True, null=True)
    text = models.TextField(verbose_name='Comment text')
    date = models.DateTimeField(auto_now=True, verbose_name='Date&Time of comment')
    moder = models.BooleanField(verbose_name='visibility', default=False)

from django.db import models
from django.contrib.auth.models import User

from recipe.models import BaseModel


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "blog category"
        verbose_name_plural = "blog categories"
    
class BlogHashgtagModel(BaseModel):
    title = models.CharField(max_length=128)


class BlogModel(BaseModel):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='blogs',null=True,blank=True)
    image = models.ImageField(upload_to="blogs")
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    hashtags = models.ManyToManyField(BlogHashgtagModel,related_name="blogs")


def __str__(self):
    return self.title

class Meta:
    verbose_name = 'blog'
    verbose_name_plural = 'blogs'


class BlogCommentModel(BaseModel):
    blog = models.ForeignKey(
        BlogModel,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    comment = models.TextField(default="Default comment")

    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True, blank=True,
        related_name='blog_comments'
    )
    

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

class BlogLikesModel(BaseModel):
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name='likes'
    )


    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='blog_likes'
    )

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
        unique_together = ['blog', 'user']
        

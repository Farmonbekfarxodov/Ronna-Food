from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ContactModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

class AboutModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


  
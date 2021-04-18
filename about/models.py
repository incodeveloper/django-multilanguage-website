from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', blank=False, null=False)
    alt = models.CharField(max_length=100, verbose_name='Alt', blank=False, null=False)
    detail = models.TextField(verbose_name='Detail', blank=False, null=False)

    name = models.CharField(max_length=100, verbose_name='Fullname', blank=False, null=False)
    location = models.CharField(max_length=100, verbose_name='Location', blank=False, null=False)
    age = models.IntegerField(max_length=2, verbose_name='Age', blank=False, null=False)
    email = models.EmailField(max_length=120, verbose_name='email', blank=False, null=False)

    twitter = models.URLField(max_length=255, verbose_name='Twitter', blank=False, null=True)
    instagram = models.URLField(max_length=255, verbose_name='Instagram', blank=False, null=True)
    facebook = models.URLField(max_length=255, verbose_name='Facebook', blank=False, null=True)
    linkedin = models.URLField(max_length=255, verbose_name='Linkedin', blank=False, null=True)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

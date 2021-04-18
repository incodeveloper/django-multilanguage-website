from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Row Name', blank=False, null=False)
    phone = models.CharField(max_length=50, verbose_name='Call Me', blank=False, null=False)
    email = models.EmailField(max_length=100, verbose_name='E-Mail Me', blank=False, null=False)
    location = models.CharField(max_length=255, verbose_name='Location', blank=False, null=False)


    def __str__(self):
        return self.name

from django.db import models
from managers import ActiveLinkManager

# Create your models here.

class Link(models.Model):
    #DB fields
    objects = models.Manager()

    public = ActiveLinkManager()
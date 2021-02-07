from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime


class images_caption(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name='Image')
    uploaded_at = models.DateTimeField(verbose_name='Uploaded Image', auto_created=True,
                                       default=datetime.datetime.now())
    caption = models.TextField(verbose_name='Caption', null=True, blank=True)
    keyword = ArrayField(verbose_name='Keywords', base_field=models.TextField(), default=list)

from django.db import models
from uuid import uuid4
from django.db.models import F

class ImageTag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

def upload_to(instance, filename):
    return 'images/%s/%s' % (uuid4(), filename)

class Image(models.Model):
    image = models.ImageField(upload_to=upload_to)
    tags = models.ManyToManyField(ImageTag, blank=True)
    def __str__(self):
        return self.image.url

class Gallery(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk:  # if this is not a new object
            old_order = GalleryImage.objects.get(pk=self.pk).order
            if self.order != old_order:  # if the order has been changed
                # increment the order of the images that have an order greater than or equal to the new order
                GalleryImage.objects.filter(gallery=self.gallery, order__gte=self.order).exclude(pk=self.pk).update(order=F('order') + 1)
        else:  # if this is a new object
            max_order = GalleryImage.objects.filter(gallery=self.gallery).aggregate(Max('order'))['order__max']
            if max_order is None:
                max_order = 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']

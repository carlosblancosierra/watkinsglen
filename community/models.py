from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True, default='Raleigh')
    state = models.CharField(max_length=255, null=True, blank=True, default='NC')
    zip = models.CharField(max_length=5, null=True, blank=True)
    lat = models.TextField(null=True, blank=True)
    long = models.TextField(null=True, blank=True)
    image_front_landspace = models.ImageField(upload_to='community-images/', null=True, blank=True)
    image_front_portrait = models.ImageField(upload_to='community-images/', null=True, blank=True)
    address = models.ForeignKey('address.Address', on_delete=models.PROTECT , null=True, blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name}, {self.city}, {self.active}"

    class Meta:
        ordering = ['order']

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Community.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Community)
def pre_save_community_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

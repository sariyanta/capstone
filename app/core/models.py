from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class User(AbstractUser):
    pass


class Place(models.Model):
    """
    A model for Places of Interest
    """

    author = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="places",
        verbose_name="Author",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Place name",
        help_text="The name of the place",
    )
    description = models.TextField(
        verbose_name="Place description",
    )
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super(Place, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

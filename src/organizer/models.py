from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField, TextField, DateField, EmailField, ManyToManyField


class Tag(models.Model):

    name = CharField(max_length=31, unique=True, default="tag-django")
    slug = AutoSlugField(max_length=31, unique=True, populate_from=["name"])

    def __str__(self):
        return self.name


class Startup(models.Model):

    name = CharField(max_length=31, db_index=True)
    slug = AutoSlugField(max_length=31, unique=True, populate_from=["name"])
    description = TextField()
    date_founded = DateField(auto_now_add=True)
    contact = EmailField()
    tags = ManyToManyField(Tag, related_name="tags")

    class Meta:
        get_latest_by = ["date_founded"]

    def __str__(self):
        return self.name

    
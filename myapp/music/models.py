from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField('Artist name', max_length=100)
    description = models.TextField('Description')
    photo = models.ImageField('Photo', upload_to='artists/%Y/%m/%d/')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField('Published', default=True)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_page', kwargs={'post_id': self.pk})

    class Meta:
        ordering = ['-time_created']


class Genre(models.Model):
    name = models.CharField('Genre name', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_page', kwargs={'genre_id': self.pk})

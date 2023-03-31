from timezone_field import TimeZoneField

from .services import times

from django.db import models


class Day(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    utc_time = TimeZoneField(use_pytz=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Cafe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='cafes')

    def __str__(self):
        return self.name


class Promo(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True, max_length=256)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='promos')
    image = models.ImageField(blank=True, null=True)
    start_time = models.TimeField(choices=times.get_start_end_times())
    end_time = models.TimeField(choices=times.get_start_end_times())
    days = models.ManyToManyField(Day)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        unique_together = ('title', 'cafe')

    def __str__(self):
        return self.title

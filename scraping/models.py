from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ќазвание населенного пункта',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta():
        verbose_name = 'Ќазвание населенного пункта'
        verbose_name_plural = 'Ќазвани€ населенных пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='язык программировани€',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta():
        verbose_name = 'язык программировани€'
        verbose_name_plural = 'языки программировани€'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)
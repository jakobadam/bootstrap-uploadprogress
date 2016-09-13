import re

from django.db import models
from django.core.validators import RegexValidator

RE_PACKAGE_NAME = re.compile(r'^[-a-zA-Z0-9_() .]+$')

class Package(models.Model):

    class Meta:
        ordering = ('name',)

    name = models.CharField(
        db_index=True,
        max_length=512,
        verbose_name='Software name',
        validators=[RegexValidator(RE_PACKAGE_NAME, 'Use ASCII characters only')]
        )

    file = models.FileField(
        verbose_name='File'
    )

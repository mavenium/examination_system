from django.db import models
from django.utils.translation import ugettext_lazy as _


class FourOptions(models.IntegerChoices):
    ONE = 1, _('One')
    TWO = 2, _('Two')
    THREE = 3, _('Three')
    FOUR = 4, _('Four')

    __empty__ = '---------'

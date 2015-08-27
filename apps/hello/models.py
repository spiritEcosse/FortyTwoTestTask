from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    surname = models.CharField(max_length=100, verbose_name=_('Surname'))
    birthday = models.DateField(verbose_name=_('Date of birth day'), blank=True, null=True)
    bio = models.TextField(verbose_name=_('Bio'), blank=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    jabber_id = models.CharField(max_length=100, verbose_name=_('Jabber id'), blank=True)
    skype_id = models.CharField(max_length=100, verbose_name=_('Skype id'), blank=True)
    contacts = models.TextField(verbose_name=_('Contacts'), blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
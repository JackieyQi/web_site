from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CConfig(models.Model):
	site = models.OneToOneField(Site, related_name='config')
	logo = models.ImageField(_('LOGO'), upload_to='upload/config/logo/%Y/%M/%D',
							 width_field='width', height_field='height', null=True, blank=True)
	logo_active = models.BooleanField(_('Logo Active'), default=True)
	description = models.CharField(_('Description'), max_length=150)
	address = models.CharField(_('Address'), max_length=50)
	phone = models.CharField(_('Phone'), max_length=50)
	width = models.PositiveIntegerField(_('Width'), default=0, blank=True)
	height = models.PositiveIntegerField(_('Height'), default=0, blank=True)

	def __unicode__(self):
		return self.site.name

	def clean(self):
		self.description = self.description.strip()
		self.address = self.address.strip()
		self.phone = self.phone.strip()

	def login_original_url(self):
		return self.logo.url

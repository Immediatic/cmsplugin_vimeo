from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

from cmsplugin_vimeo import settings

class Vimeo(CMSPlugin):
    video_id = models.CharField(_('video id'), max_length=60)

    autoplay = models.BooleanField(
        _('autoplay'),
        default=settings.CMS_VIMEO_DEFAULT_AUTOPLAY
    )

    width = models.IntegerField(_('width'),
            default=settings.CMS_VIMEO_DEFAULT_WIDTH)
    height = models.IntegerField(_('height'),
            default=settings.CMS_VIMEO_DEFAULT_HEIGHT)
    border = models.BooleanField(_('border'),
            default=settings.CMS_VIMEO_DEFAULT_BORDER)

    loop = models.BooleanField(_('loop'),
        default=settings.CMS_VIMEO_DEFAULT_LOOP)

    def __unicode__(self):
        return u'%s' % (self.video_id,)

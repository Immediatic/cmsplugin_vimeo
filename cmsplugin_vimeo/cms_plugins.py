from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_vimeo.models import Vimeo as VimeoModel

from django.utils.translation import ugettext as _

class VimeoPlugin(CMSPluginBase):
    model = VimeoModel
    name = _("Vimeo")
    render_template = "cmsplugin_vimeo/embed.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(VimeoPlugin)

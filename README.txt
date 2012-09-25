cmsplugin_vimeo
===============

Plugin for Django CMS that makes easy to embed Vimeo movies.

Download: https://github.com/Immediatic/cmsplugin_vimeo

Requirements:
- django-cms-2.3 or greater
- django: 1.4 or greater

Last tested with:
- django-cms-2.3.1
- django: 1.4.1

Setup
-----

- make sure requirements are installed and properly working
- add cmsplugin_vimeo to python path
- add 'cmsplugin_vimeo' to INSTALLED_APPS
- run 'python manage.py migrate cmsplugin_vimeo' if using South or 'python manage.py syncdb' if not using South

Settings
--------

- CMS_VIMEO_DEFAULT_AUTOPLAY      (Default False)
- CMS_VIMEO_DEFAULT_WIDTH         (Default 425)
- CMS_VIMEO_DEFAULT_HEIGHT        (Default 344)
- CMS_VIMEO_DEFAULT_BORDER        (Default False)
- CMS_VIMEO_DEFAULT_LOOP          (Default False)

Credits
-------

This plugin derives from [cmsplugin-youtube](https://bitbucket.org/xenofox/cmsplugin-youtube) and has been customized for Vimeo movies.

The plugin is available on [Django Packages](http://www.djangopackages.com/packages/p/cmsplugin_vimeo/).

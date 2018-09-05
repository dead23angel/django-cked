# coding: utf8
from django import forms
from django.conf import settings
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.template.loader import render_to_string

try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from django.core.exceptions import ImproperlyConfigured
try:
    from django.forms.util import flatatt
except ImportError:
    from django.forms.utils import flatatt

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from cked import default_settings


json_encode = json.JSONEncoder().encode


class CKEditorWidget(forms.Textarea):
    """
Widget providing CKEditor for Rich Text Editing.
"""
    class Media:
        js = (settings.STATIC_URL + 'cked/ckeditor/ckeditor.js',)

    def __init__(self, *args, **kwargs):
        super(CKEditorWidget, self).__init__(*args, **kwargs)
        # Use default config
        self.options = default_settings.CKEDITOR_DEFAULT_OPTIONS.copy()

        # If CKEDITOR_OPTIONS presented in settings, use it!
        options = getattr(settings, 'CKEDITOR_OPTIONS', None)

        if options is not None:
            if isinstance(options, dict):
                # Override defaults with CKEDITOR_OPTIONS.
                self.options.update(options)
            else:
                raise ImproperlyConfigured('CKEDITOR_OPTIONS setting must be'
                                           ' a dictionary type.')

    def render(self, name, value, attrs={}, renderer=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(self.attrs, attrs, name=name)

        self.options['filebrowserBrowseUrl'] = reverse('cked_elfinder')

        return mark_safe(render_to_string('cked/ckeditor.html', {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_unicode(value)),
            'id': final_attrs['id'],
            'options': json_encode(self.options)})
        )

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        """
        Helper function for building an attribute dictionary.
        This is combination of the same method from Django<=1.10 and Django1.11+
        """
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

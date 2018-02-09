# coding: utf8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from cked import elFinder
from cked.widgets import json_encode
from cked import default_settings

try:
    import json
except ImportError:
    from django.utils import simplejson as json


json_encode = json.JSONEncoder().encode


@login_required(login_url='/login')
def elfinder(request):
    options = default_settings.ELFINDER_DEFAULT_OPTIONS.copy()
    options['url'] = reverse('cked_elfinder_connector')

    user_options = getattr(settings, 'ELFINDER_OPTIONS', None)

    if user_options is not None:
        if isinstance(user_options, dict):
            # Override defaults with CKEDITOR_OPTIONS.
            options.update(user_options)
        else:
            raise ImproperlyConfigured('CKEDITOR_OPTIONS setting must be a '
                                       'dictionary type.')

    return render(request, 'cked/elfinder.html', {
        'options': json_encode(options),
    })


@csrf_exempt
@login_required
def elfinder_connector(request):
    elf = elFinder.connector(settings.ELFINDER_OPTIONS)
    req = {}

    if request.method == 'GET':
        form = request.GET
    else:
        form = request.POST

    for field in elf.httpAllowedParameters:
        if field in form:
            req[field] = form.get(field)

            # Hack by Kidwind
            if field == 'targets[]' and hasattr(form, 'getlist'):
                req[field] = form.getlist(field)

    if request.FILES and request.FILES.getlist('upload[]'):
        up_files = {}
        for up in request.FILES.getlist('upload[]'):
            if up.name:
                up_files[up.name] = up.file

        req[field] = up_files

    status, header, response = elf.run(req)

    if not response is None and status == 200:
        if 'file' in response and isinstance(response['file'], file):
            response['file'].close()

    return HttpResponse(json.dumps(response), content_type='application/json')

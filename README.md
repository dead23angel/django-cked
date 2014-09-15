Django CKEd
===========

![alt text](https://pypip.in/version/django-cked/badge.svg "Latest Version")
![alt text](https://pypip.in/download/django-cked/badge.svg "Downloads")
![alt text](https://pypip.in/py_versions/django-cked/badge.svg "Supported Python versions")
![alt text](https://pypip.in/status/django-cked/badge.svg "Development Status")
![alt text](https://pypip.in/license/django-cked/badge.svg "License")

**CKEditor and elFinder integration for Django Framework.**

Provides a **RichTextField** and **CKEditorWidget** with upload and
browse support.

![alt text](https://bitbucket.org/CWTeam/django-cked/raw/default/img/ckeditor.jpg "CKEditor")
![alt text](https://bitbucket.org/CWTeam/django-cked/raw/default/img/elfinder.jpg "elFinder")

Installation
------------

```python

    pip install django-cked

```

or

```python

    pip install -e hg+https://bitbucket.org/CWTeam/django-cked#egg=django-cked
    
```

Configuration
-------------

Add **cked** to your **INSTALLED_APPS** setting.

Then set **ELFINDER_OPTIONS** in your settings:

```python

    ELFINDER_OPTIONS = {
        ## required options
        'root': os.path.join(PROJECT_ROOT, 'media', 'uploads'),
        'URL': '/media/uploads/',
    }

```

And add CKEd URL include to your project **urls.py** file:

```python

    url(r'^cked/', include('cked.urls')),
    
```

Settings
--------

-  **CKEDITOR\_OPTIONS**: CKEditor config. See
   http://docs.ckeditor.com/#!/guide/dev_configuration
-  **ELFINDER\_OPTIONS**: elFinder config. See
   https://github.com/Studio-42/elFinder/wiki/Client-configuration-options

Usage
-----

Model field
~~~~~~~~~~~

```python

    from django.db import models
    from cked.fields import RichTextField


    class Entry(models.Model):
        text = RichTextField()
        
```

Widget
~~~~~~

```python

    from django import forms
    from cked.widgets import CKEditorWidget

    class MyForm(forms.Form):
        text = forms.CharField(widget=CKEditorWidget)

```

**NOTE**: If you are using custom forms, dont’r forget to include form
media to your template:

```python

    {{ form.media }}
    
```

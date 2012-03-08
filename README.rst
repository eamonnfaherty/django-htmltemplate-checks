=======
django-htmltemplate-checks
=======

django-htmltemplate-checks is a `Django <http://www.djangoproject.com/>`_ application that adds basicc checks to your html for quality assurance.


********
Checks
********

* check_a_tags - checks a tags for alt attributes
* check_img_tags - checks img tags for title attributes


************
Requirements
************

* any version of Django, but was tested with Django 1.3
* needs BeautifulSoup for HTML parsing.

************
Installation
************


1. ``pip install django-htmltemplate-checks``
2. Add ``'htmltemplate'`` to the `INSTALLED_APPS` in your project's ``settings.py``

To uninstall, simply comment out or remove the ``'htmltemplate'`` line in your ``INSTALLED_APPS``

*************
Running
*************

* manage.py check_a_tags
* manage.py check_img_tags

import os
from BeautifulSoup import BeautifulSoup
import settings

def check_tag_attribute(tag, attribute):
    """
    For given tag check all templates for existence of attribute
    """
    print "checking TEMPLATE_DIRS"
    for dir_to_walk in settings.TEMPLATE_DIRS:
        check_dir(dir_to_walk, tag, attribute)

    if should_check_installed_apps():
        print "checking INSTALLED apps"
        for app in settings.INSTALLED_APPS:
            if '.' in app:
                dir_to_walk = app.split(".")[-1]
            else:
                dir_to_walk = app
            check_dir(dir_to_walk, tag, attribute)

def should_check_installed_apps():
    """
    Checks to see if 'django.template.loaders.app_directories.Loader' is in TEMPLATE_LOADERS
    """
    loader = 'django.template.loaders.app_directories.Loader'
    should_check_installed_apps = loader in settings.TEMPLATE_LOADERS

    if not should_check_installed_apps:
        for first_level in settings.TEMPLATE_LOADERS:
            if not should_check_installed_apps:
                should_check_installed_apps = loader in first_level
                if not should_check_installed_apps:
                    for second_level in first_level:
                        if not should_check_installed_apps:
                            should_check_installed_apps = loader in second_level
    return should_check_installed_apps


def check_file(file_to_check, tag, attribute):
    """
    Given a string file_to_check this function checks all tags named tag for the existence of an attribute called
    attribute
    """
    soup = BeautifulSoup(BeautifulSoup(open(file_to_check)).prettify())
    errors = 0
    for tag in soup.findAll(tag):
        try:
            if tag[attribute] == "":
                errors += 1
        except KeyError:
            errors += 1

    if errors > 0:
        print "\t%s : %s" % (file_to_check, errors)


def check_dir(dir_to_walk, tag, attribute):
    """
    Give a string dir_to_walk this function checks all files within for tags named tag for the existence of an attribute
    called attribute
    """
    for root, dirs, files in os.walk(dir_to_walk):
        for file in files:
            file_to_check = u"%s/%s" % (root,file)
            check_file(file_to_check, tag, attribute)
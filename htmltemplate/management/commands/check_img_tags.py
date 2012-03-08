from django.core.management.base import BaseCommand
from htmltemplate.management.commands.utils import check_tag_attribute

class Command(BaseCommand):
    help = 'checks img tags for the alt attribute'
    args = 'Nothing...'

    def handle(self, *args, **kwargs):
        check_tag_attribute('img', 'alt')
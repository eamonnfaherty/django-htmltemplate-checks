from django.core.management.base import BaseCommand
from htmltemplate.management.commands.utils import check_tag_attribute

class Command(BaseCommand):
    help = 'checks a tags for the title attribute'
    args = 'Nothing...'

    def handle(self, *args, **kwargs):
        check_tag_attribute('a', 'title')
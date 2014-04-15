from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for poll_id in args:
            try:
                poll = poll_id
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            self.stdout.write('Successfully closed poll "%s"' % poll_id)

# print Command()
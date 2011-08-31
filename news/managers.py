from django.db.models import Manager
import datetime

class PublicManager(Manager):
    '''Returns published articles that are not in the future.'''

    def published(self):
        return self.get_query_set().filter(status__gte=2, pub_date__lte=datetime.datetime.now()).order_by('-pub_date')


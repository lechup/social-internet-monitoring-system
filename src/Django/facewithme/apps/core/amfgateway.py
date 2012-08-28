from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from pyamf.remoting.gateway.django import DjangoGateway

from apps.core.models import Entry, Category
from lib.slughifi import slughifi


@transaction.commit_on_success
def start_broadcasting(request, title, is_public, coordinates = [], categories = [], username = None, password = None):
    u"""
        Checks if title is available name for broadcasting
        returns None on failure or object reserved for broadcasting,
    """
    
    if not title or len(title) < 5:
        return None
    
    entry = {
        'title' : title,
        'is_public' : is_public,
        'user' : None
    }

    # check for username and password
    if username and password:
        try:
            entry['user'] = User.objects.get(username = username, password = password)
        except ObjectDoesNotExist:
            return None
    
    slug = slughifi(title)
    # if slug is unique?
    if Entry.objects.filter(slug = slug).count() == 0:
        new_entry = Entry.objects.create(**entry)
        new_entry.save()
        # add categories
        for category in Category.objects.filter(value__in = list(categories)):
            new_entry.categories.add(category)
        return {
            'uuid': new_entry.uuid,
            'server': new_entry.server.url,
            'url': new_entry.get_absolute_url(),
        }
    else:
        return None


def check_login_and_password(request, username = None, password = None):
    if User.objects.filter(username = username, password = password).count() == 1:
        return True
    else:
        return False


def stop_broadcasting(request, uuid):
    if uuid:
        Entry.objects.filter(uuid = uuid).delete()
    return True


def start_receiving(request, uuid):
    try:
        entry = Entry.objects.get(uuid = uuid)
    except ObjectDoesNotExist:
        return None

    return {
        'uuid': entry.uuid,
        'server': entry.server.url,
        'url': entry.get_absolute_url(),
    }


def stop_receiving(request, uuid):
    return True


def update_coordinates(request, uuid, lng, lat):
    try: 
        entry = Entry.objects.get(uuid = uuid)
    except ObjectDoesNotExist:
        return False
    else:
        entry.coordinates.x = lng
        entry.coordinates.y = lat
        entry.save()
        return True


# variable used in settings/urls.py
# without authentication
services = DjangoGateway({
        'fwm.start_broadcasting': start_broadcasting,
        'fwm.stop_broadcasting': stop_broadcasting,
        'fwm.start_receiving': start_receiving,
        'fwm.stop_receiving': stop_receiving,
        'fwm.check_login_and_password': check_login_and_password,
        'fwm.update_coordinates': update_coordinates,
    }
)

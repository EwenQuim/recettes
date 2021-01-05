"""
Parsing data
"""

from django.http import Http404


def parse_slug(slug):
    """ Parse the slug and return the list of recipe ids"""

    week = slug.split("-")[:14]

    # Convert to int
    for k, meal in zip(range(len(week)), week):
        try:
            week[k] = int(meal)
        except ValueError as not_only_ints:
            raise Http404 from not_only_ints

    # Not long enough ?
    while not len(week) == 14:
        week.append(0)
    return week

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



# گیت هاب پیج
# https://data-hub.ir/how-to-host-a-website-on-github/




# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


# python manage.py startapp Course


# https://pages.github.com/

# https://www.aparat.com/v/ykuIN

# http://shop-center.whi.ir/

# https://hostiran.net/profile/panel/service/152088/detail?state=info
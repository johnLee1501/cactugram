#!/usr/bin/env bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
  (cd cactugram;  python manage.py createsuperuser --no-input)
  fi
(cd cactugram; gunicorn cactugram.wsgi --user www-data --bind 0.0.0.0:8019 --workers 3) &
nginx -g "daemon off;"

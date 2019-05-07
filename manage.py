#!/usr/bin/env python3.7
import os, sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
    os.environ.setdefault('DJANGO_SETTINGS_ENVIRONMENT', 'dev')

    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

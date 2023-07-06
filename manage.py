#!/usr/bin/env python
"""Django's command-line utilidad para control de tareas."""
import os
import sys


def main():
    """Run tareas de adminstracion."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
             "No se pudo importar Django. ¿Estás seguro de que está instalado y "
             "disponible en su variable de entorno PYTHONPATH? ¿Lo hizo?"
             "¿Olvidaste activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

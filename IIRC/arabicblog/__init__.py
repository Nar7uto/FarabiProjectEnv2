import pkg_resources


__version__ = pkg_resources.get_distribution("arabicblog").version
default_app_config = "arabicblog.apps.AppConfig"

from django.apps import AppConfig


class CeiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cei'

    def ready(self) -> None:
        print('APP READY - ', self.name)
        import sys
        if not 'makemigrations' in sys.argv and not 'migrate' in sys.argv and not 'collectstatic' in sys.argv and not 'datamigration' in sys.argv:
            from cei.ceischeduled import CeiScheduled
            CeiScheduled().start()
        return super().ready()
        

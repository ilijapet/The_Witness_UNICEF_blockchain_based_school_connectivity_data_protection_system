import sys

from apscheduler.events import EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

from iot_data_generator.task import IotDataGenerator


class IotDataGeneratorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "iot_data_generator"

    def handle_errors(self, event):
        print(f"Error occurred in job: {event.job_id}")
        print(f"Exception: {event.exception}")
        print(f"Traceback: {event.traceback}")

    def ready(self):
        if "runserver" in sys.argv:
            scheduler = BackgroundScheduler()
            iot = IotDataGenerator()
            scheduler.add_job(iot.iot_data_generator, "interval", seconds=30)
            scheduler.add_listener(self.handle_errors, EVENT_JOB_ERROR)
            scheduler.start()

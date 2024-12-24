from django.db import models


class NetworkData(models.Model):
    school_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    download_speed = models.FloatField()
    upload_speed = models.FloatField()
    latency = models.FloatField()
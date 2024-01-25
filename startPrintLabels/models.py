from datetime import datetime

from django.db import models


class Codes(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=85, unique=True)
    printed_out = models.BooleanField(default=False)
    id_sku = models.IntegerField(default=0)
    id_party = models.IntegerField(default=0)
    date_loaded = models.DateTimeField(auto_now_add=True)
    date_output = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.code} print-{self.printed_out}'

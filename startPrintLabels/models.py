from datetime import datetime

from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    full_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.full_name


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    sort = models.IntegerField(default=0)
    cut = models.CharField(max_length=3, default='')

    def __str__(self):
        return f'{self.name} - {self.cut}'


class Parts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    prefix = models.CharField(max_length=30, default='')
    number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.prefix} - {self.prefix} - {self.date_added}'


class FileLoad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.name}'


class SKU(models.Model):
    id = models.AutoField(primary_key=True)
    gtin = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=150, default='')
    prefix = models.CharField(max_length=5, default='')
    id_groups = models.ForeignKey(Groups, on_delete=models.CASCADE)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gtin} - {self.name}'


class Codes(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=85, unique=True)
    printed_out = models.BooleanField(default=False)
    id_sku = models.ForeignKey(SKU, on_delete=models.CASCADE, null=True)
    id_parts = models.ForeignKey(Parts, on_delete=models.CASCADE, null=True)
    date_loaded = models.DateTimeField(auto_now_add=True)
    date_output = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'code - {self.code}; print-{self.printed_out}; date-{self.date_loaded.strftime("%d.%b.%y")}'

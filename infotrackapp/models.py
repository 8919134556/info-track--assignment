from django.db import models
from datetime import datetime


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    header1 = models.CharField(verbose_name='Header1', db_column="header1", max_length=50, blank=False,
                                  null=False)

    header2 = models.CharField(verbose_name='Header2', db_column="header2", max_length=50, blank=False,
                                  null=False)
    
    header3 = models.CharField(verbose_name='Header3', db_column="header3", max_length=50, blank=False,
                                  null=True)
    
    header4 = models.CharField(verbose_name='Header4', db_column="header4", max_length=50, blank=False,
                                  null=True)
    
    header5 = models.CharField(verbose_name='Header5', db_column="header5", max_length=50, blank=False,
                                  null=False)
    header6 = models.CharField(verbose_name='Header6', db_column="header6", max_length=50, blank=False,
                                  null=False)
    class Meta:
        db_table='Data'
    

class Select_data(models.Model):
    id = models.AutoField(primary_key=True)
    
    no = models.CharField(verbose_name='No', db_column="no", max_length=50, blank=False,
                                  null=True)
    header1 = models.CharField(verbose_name='Header1', db_column="header1", max_length=50, blank=False,
                                  null=False)

    header2 = models.CharField(verbose_name='Header2', db_column="header2", max_length=50, blank=False,
                                  null=False)
    
    header3 = models.CharField(verbose_name='Header3', db_column="header3", max_length=50, blank=False,
                                  null=True)
    
    header4 = models.CharField(verbose_name='Header4', db_column="header4", max_length=50, blank=False,
                                  null=True)
    
    header5 = models.CharField(verbose_name='Header5', db_column="header5", max_length=50, blank=False,
                                  null=False)
    header6 = models.CharField(verbose_name='Header6', db_column="header6", max_length=50, blank=False,
                                  null=False)
    class Meta:
        db_table='Select_data'
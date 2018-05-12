# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Recom_guide(models.Model):
	questionId = models.IntegerField(default=0)
	sentence = models.CharField(max_length=60,null=True)
	count = models.IntegerField(default=0)
	value = models.FloatField(default=0.0)
	epsilon = models.FloatField(default=0.3)
	gamma = models.FloatField(default=0.3)
	weight = models.FloatField(default=1.0)
	temperature = models.FloatField(default=0.3)
	alpha = models.FloatField(default=0.5)
	current_arm = models.IntegerField(default=0)
	next_update = models.IntegerField(default=0)
	r = models.IntegerField(default=0)
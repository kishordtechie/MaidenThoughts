# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20151018_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

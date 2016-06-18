# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(verbose_name=b'date published')),
                ('images', models.ImageField(max_length=200, upload_to=b'photos/%Y/%m/%d')),
                ('content', models.TextField(max_length=10000)),
                ('tags', models.CharField(max_length=200)),
                ('viewed_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(verbose_name=b'date published')),
                ('images', models.ImageField(max_length=200, upload_to=b'photos/%Y/%m/%d')),
                ('content', models.TextField(max_length=10000)),
                ('tags', models.CharField(max_length=200)),
                ('viewed_count', models.IntegerField()),
                ('author', models.ForeignKey(to='webapp.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='type',
            field=models.ForeignKey(to='webapp.Types'),
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(to='webapp.Authors'),
        ),
        migrations.AddField(
            model_name='articles',
            name='type',
            field=models.ForeignKey(to='webapp.Types'),
        ),
    ]

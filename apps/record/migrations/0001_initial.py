# Generated by Django 2.0.5 on 2018-05-05 00:56

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(default='end', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StartRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(default='start', max_length=5)),
                ('source', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)])),
                ('destination', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
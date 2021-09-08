# Generated by Django 3.1.10 on 2021-09-08 20:38

import json

import django.db.models.deletion
from django.db import migrations, models

import bike.models


def populate(apps, schema_editor):
    Bike = apps.get_model('bike', 'Bike')
    Fleet = apps.get_model('fleet', 'Fleet')
    db_alias = schema_editor.connection.alias

    file = open('core/data.json')
    data = json.load(file)

    for bike in data['bikes']:
        fleet = Fleet.objects.using(db_alias).get(id=bike['fleet'])
        Bike.objects.using(db_alias).create(
            id=bike['id'], fleet=fleet,
            status=bike['status'], location=bike['location']
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.CharField(default=bike.models.generate_id, editable=False, help_text='id', max_length=6, primary_key=True, serialize=False, verbose_name='id')),
                ('status', models.CharField(choices=[('unlocked', 'unlocked'), ('locked', 'locked')], help_text='status', max_length=8, verbose_name='status')),
                ('location', models.JSONField(help_text='location', verbose_name='location')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='updated', verbose_name='updated')),
                ('archived', models.BooleanField(default=False, help_text='archived', verbose_name='archived')),
                ('fleet', models.ForeignKey(blank=True, help_text='fleet', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bike', to='fleet.fleet', verbose_name='fleet')),
            ],
            options={
                'verbose_name': 'bike',
                'verbose_name_plural': 'bikes',
                'db_table': 'bike.bikes',
            },
        ),
        migrations.RunPython(populate)
    ]
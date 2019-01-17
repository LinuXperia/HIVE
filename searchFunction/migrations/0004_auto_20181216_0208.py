# Generated by Django 2.1.2 on 2018-12-16 02:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchFunction', '0003_auto_20181216_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='items_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indexKey', models.IntegerField(db_index=True, default=0)),
                ('item', models.TextField(default='')),
                ('itemVector', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='clinicaltrial',
            name='ctVector',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='grantVector',
        ),
        migrations.RemoveField(
            model_name='investigator',
            name='authorVector',
        ),
        migrations.AlterField(
            model_name='terms_list',
            name='termVector',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None),
        ),
    ]

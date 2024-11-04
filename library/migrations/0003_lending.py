# Generated by Django 5.1.1 on 2024-11-04 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lending_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='out', max_length=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.client')),
            ],
        ),
    ]

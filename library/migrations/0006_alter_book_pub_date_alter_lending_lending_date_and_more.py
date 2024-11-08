# Generated by Django 5.1.3 on 2024-11-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lending',
            name='lending_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lending',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
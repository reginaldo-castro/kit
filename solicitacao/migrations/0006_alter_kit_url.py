# Generated by Django 4.0.5 on 2022-06-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0005_kit_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kit',
            name='url',
            field=models.CharField(max_length=250, verbose_name='url'),
        ),
    ]

# Generated by Django 3.1.6 on 2024-12-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20241225_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-17 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iceapp', '0003_churchandotherbuilding_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='majorcelebrationhistoricalevent',
            old_name='introduction',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='majorcelebrationhistoricalevent',
            old_name='introduction_image',
            new_name='about_image',
        ),
    ]

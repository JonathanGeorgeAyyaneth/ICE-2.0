# Generated by Django 5.0.7 on 2024-08-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iceapp', '0005_remove_churchandotherbuilding_events_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='category',
            field=models.CharField(blank=True, choices=[('Diocese', 'Diocese'), ('Basilica', 'Basilica'), ('Cathedrals', 'Cathedrals'), ('Parishes', 'Parishes'), ('Pilgrime Centers', 'Pilgrime Centers'), ('Congregations', 'Congregations'), ('Pios Associations', 'Pios Associations')], max_length=60, null=True),
        ),
    ]

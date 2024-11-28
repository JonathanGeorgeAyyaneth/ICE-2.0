# Generated by Django 5.0.7 on 2024-08-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iceapp', '0007_alter_churchandotherbuilding_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionbuilding',
            name='category',
            field=models.CharField(choices=[('Universities', 'Universities'), ('Colleges', 'Colleges'), ('Schools', 'Schools'), ('Technical Institutions', 'Technical Institutions'), ('Medical Colleges', 'Medical Colleges'), ('Hospitals', 'Hospitals'), ('Charity Institutions', 'Charity Institutions')], default='Colleges', max_length=50),
            preserve_default=False,
        ),
    ]

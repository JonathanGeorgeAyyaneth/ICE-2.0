# Generated by Django 5.0.7 on 2024-08-03 04:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iceapp', '0002_alter_churchandotherbuilding_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='created_by',
            field=models.CharField(default='jonathan', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='churchcommunity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchcommunity',
            name='created_by',
            field=models.CharField(default='jonathan', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchcommunity',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='churchcommunity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='created_by',
            field=models.CharField(default='jonathan', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='majorcelebrationhistoricalevent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='majorcelebrationhistoricalevent',
            name='created_by',
            field=models.CharField(default='jonathan', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='majorcelebrationhistoricalevent',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='majorcelebrationhistoricalevent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=models.CharField(default='jonathan', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchAndOtherBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('history', models.TextField()),
                ('history_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('architecture_and_design', models.TextField()),
                ('architecture_and_design_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('functions_and_services', models.TextField()),
                ('functions_and_services_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('community_impact', models.TextField()),
                ('community_impact_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('governance_and_leadership', models.TextField()),
                ('governance_and_leadership_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('notable_features', models.TextField()),
                ('notable_features_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
                ('conclusion', models.TextField()),
                ('conclusion_image', models.ImageField(blank=True, null=True, upload_to='church_and_other_building/')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchCommunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('governance_and_structure', models.TextField()),
                ('governance_and_structure_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('worship_practices_and_rituals', models.TextField()),
                ('worship_practices_and_rituals_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('beliefs_and_teachings', models.TextField()),
                ('beliefs_and_teachings_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('community_life', models.TextField()),
                ('community_life_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('historical_figures', models.TextField()),
                ('historical_figures_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
                ('conclusion', models.TextField()),
                ('conclusion_image', models.ImageField(blank=True, null=True, upload_to='church_community/')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('history', models.TextField()),
                ('history_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('mission_and_values', models.TextField()),
                ('mission_and_values_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('services_and_programs', models.TextField()),
                ('services_and_programs_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('impact_and_reach', models.TextField()),
                ('impact_and_reach_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('governance_and_leadership', models.TextField()),
                ('governance_and_leadership_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('notable_achievements', models.TextField()),
                ('notable_achievements_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('conclusion', models.TextField()),
                ('conclusion_image', models.ImageField(blank=True, null=True, upload_to='institution_building/')),
                ('church_buildings', models.ManyToManyField(blank=True, related_name='institutions_buildings', to='iceapp.churchandotherbuilding')),
            ],
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='institutions',
            field=models.ManyToManyField(blank=True, related_name='church_buildings_institutions', to='iceapp.institutionbuilding'),
        ),
        migrations.CreateModel(
            name='MajorCelebrationHistoricalEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('introduction', models.TextField()),
                ('introduction_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('background', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('the_event', models.TextField()),
                ('the_event_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('impact_and_significance', models.TextField()),
                ('impact_and_significance_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('commemoration', models.TextField()),
                ('commemoration_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('conclusion', models.TextField()),
                ('conclusion_image', models.ImageField(blank=True, null=True, upload_to='major_celebration_historical_event/')),
                ('church_buildings', models.ManyToManyField(blank=True, related_name='events_church_buildings', to='iceapp.churchandotherbuilding')),
                ('institutions', models.ManyToManyField(blank=True, related_name='events_institutions', to='iceapp.institutionbuilding')),
            ],
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='institutions_events', to='iceapp.majorcelebrationhistoricalevent'),
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='church_buildings_events', to='iceapp.majorcelebrationhistoricalevent'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('early_life', models.TextField()),
                ('early_life_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('key_achievements', models.TextField()),
                ('key_achievements_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('influence_and_legacy', models.TextField()),
                ('influence_and_legacy_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('veneration_recognition', models.TextField()),
                ('veneration_recognition_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('personal_reflections', models.TextField()),
                ('personal_reflections_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('conclusion', models.TextField()),
                ('conclusion_image', models.ImageField(blank=True, null=True, upload_to='person/')),
                ('church_buildings', models.ManyToManyField(blank=True, related_name='people_church_buildings', to='iceapp.churchandotherbuilding')),
                ('events', models.ManyToManyField(blank=True, related_name='people_events', to='iceapp.majorcelebrationhistoricalevent')),
                ('institutionss', models.ManyToManyField(blank=True, related_name='people_institutions', to='iceapp.institutionbuilding')),
            ],
        ),
        migrations.AddField(
            model_name='majorcelebrationhistoricalevent',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='events_people', to='iceapp.person'),
        ),
        migrations.AddField(
            model_name='institutionbuilding',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='institutions', to='iceapp.person'),
        ),
        migrations.AddField(
            model_name='churchandotherbuilding',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='institutions_people', to='iceapp.person'),
        ),
    ]

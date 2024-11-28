from django.core.management.base import BaseCommand
from iceapp.models import ChurchAndOtherBuilding,ChurchCommunity,MajorCelebrationHistoricalEvent,InstitutionBuilding,Person 
from googletrans import Translator
import textwrap
class Command(BaseCommand):
    help = 'Translate existing records'

    def handle(self, *args, **kwargs):
            self.translate_institution_building()
            self.stdout.write(self.style.SUCCESS("Translation process completed for Institution Buildings"))
            self.translate_person()
            self.stdout.write(self.style.SUCCESS("Translation process completed for Person"))
            self.translate_churchandotherbuildings()
            self.stdout.write(self.style.SUCCESS("Translation process completed for Church and Other Buildings"))
            self.translate_churchcommunity()
            self.stdout.write(self.style.SUCCESS("Translation process completed for Church Community"))
            self.translate_majorcelebrations()
            self.stdout.write(self.style.SUCCESS("Translation process completed for Major Celebrations and Events"))
            self.stdout.write(self.style.HTTP_INFO("All Translations completed"))




    def translate_person(self):
        translator = Translator()
           # List of fields to translate
        fields_to_translate = [
            ('about', 'about_ml', 'about_hi'),
            ('early_life', 'early_life_ml', 'early_life_hi'),
            ('key_achievements', 'key_achievements_ml', 'key_achievements_hi'),
            ('influence_and_legacy', 'influence_and_legacy_ml', 'influence_and_legacy_hi'),
            ('veneration_recognition', 'veneration_recognition_ml', 'veneration_recognition_hi'),
            ('conclusion', 'conclusion_ml', 'conclusion_hi'),
            ('personal_reflections', 'personal_reflections_ml', 'personal_reflections_hi'),
        ]
        # Process each record
        for record in Person.objects.all():
            record_updated = False
            for field_name, ml_field, hi_field in fields_to_translate:
                original_text = getattr(record, field_name, "")
                
                # Skip translation if field is empty or already translated
                if not original_text:
                    continue
                if getattr(record, ml_field) and getattr(record, hi_field):
                    self.stdout.write(self.style.WARNING(
                        f'Skipping translation for record {record.id} - {field_name} (already translated)'
                    ))
                    continue
                try:
                    # Translate to Malayalam if not already translated
                    if not getattr(record, ml_field):
                        translated_text_ml = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='ml')
                            translated_text_ml += translated.text + " "
                        setattr(record, ml_field, translated_text_ml.strip())
                        record_updated = True
                    # Translate to Hindi if not already translated
                    if not getattr(record, hi_field):
                        translated_text_hi = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='hi')
                            translated_text_hi += translated.text + " "
                        setattr(record, hi_field, translated_text_hi.strip())
                        record_updated = True
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating {field_name} for record {record.id}: {e}"))
            # Save the updated record if any translations were made
            if record_updated:
                record.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated and updated record {record.id}'))

    
    def translate_institution_building(self):
        translator = Translator()

        fields_to_translate = [
            ('about', 'about_ml', 'about_hi'),
            ('history', 'history_ml', 'history_hi'),
            ('mission_and_values', 'mission_and_values_ml', 'mission_and_values_hi'),
            ('services_and_programs', 'services_and_programs_ml', 'services_and_programs_hi'),
            ('impact_and_reach', 'impact_and_reach_ml', 'impact_and_reach_hi'),
            ('governance_and_leadership', 'governance_and_leadership_ml', 'governance_and_leadership_hi'),
            ('notable_achievements', 'notable_achievements_ml', 'notable_achievements_hi'),
            ('conclusion', 'conclusion_ml', 'conclusion_hi'),
        ]

        for record in InstitutionBuilding.objects.all():
            record_updated = False

            for field_name, ml_field, hi_field in fields_to_translate:
                original_text = getattr(record, field_name, "")

                # Skip translation if field is empty or already translated
                if not original_text:
                    continue
                if getattr(record, ml_field) and getattr(record, hi_field):
                    self.stdout.write(self.style.WARNING(
                        f'Skipping translation for record {record.id} - {field_name} (already translated)'
                    ))
                    continue

                try:
                    # Translate to Malayalam if not already translated
                    if not getattr(record, ml_field):
                        translated_text_ml = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='ml')
                            translated_text_ml += translated.text + " "
                        setattr(record, ml_field, translated_text_ml.strip())
                        record_updated = True

                    # Translate to Hindi if not already translated
                    if not getattr(record, hi_field):
                        translated_text_hi = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='hi')
                            translated_text_hi += translated.text + " "
                        setattr(record, hi_field, translated_text_hi.strip())
                        record_updated = True

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating {field_name} for record {record.id}: {e}"))

            # Save the updated record if any translations were made
            if record_updated:
                record.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated and updated record {record.id}'))


    def translate_majorcelebrations(self):
        translator = Translator()
        
        # List of fields to translate
        fields_to_translate = [
            ('about', 'about_ml', 'about_hi'),
            ('background', 'background_ml', 'background_hi'),
            ('the_event', 'the_event_ml', 'the_event_hi'),
            ('impact_and_significance', 'impact_and_significance_ml', 'impact_and_significance_hi'),
            ('commemoration', 'commemoration_ml', 'commemoration_hi'),
            ('conclusion', 'conclusion_ml', 'conclusion_hi')
        ]

        # Process each record
        for record in MajorCelebrationHistoricalEvent.objects.all():
            record_updated = False

            for field_name, ml_field, hi_field in fields_to_translate:
                original_text = getattr(record, field_name, "")
                
                # Skip translation if field is empty or already translated
                if not original_text:
                    continue
                if getattr(record, ml_field) and getattr(record, hi_field):
                    self.stdout.write(self.style.WARNING(
                        f'Skipping translation for record {record.id} - {field_name} (already translated)'
                    ))
                    continue

                try:
                    # Translate to Malayalam if not already translated
                    if not getattr(record, ml_field):
                        translated_text_ml = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='ml')
                            translated_text_ml += translated.text + " "
                        setattr(record, ml_field, translated_text_ml.strip())
                        record_updated = True

                    # Translate to Hindi if not already translated
                    if not getattr(record, hi_field):
                        translated_text_hi = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='hi')
                            translated_text_hi += translated.text + " "
                        setattr(record, hi_field, translated_text_hi.strip())
                        record_updated = True

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating {field_name} for record {record.id}: {e}"))

            # Save the updated record if any translations were made
            if record_updated:
                record.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated and updated record {record.id}'))

    
    def translate_churchandotherbuildings(self):
        translator = Translator()
        
        # List of fields to translate
        fields_to_translate = [
            ('about', 'about_ml', 'about_hi'),
            ('history', 'history_ml', 'history_hi'),
            ('architecture_and_design', 'architecture_and_design_ml', 'architecture_and_design_hi'),
            ('functions_and_services', 'functions_and_services_ml', 'functions_and_services_hi'),
            ('community_impact', 'community_impact_ml', 'community_impact_hi'),
            ('conclusion', 'conclusion_ml', 'conclusion_hi'),
            ('governance_and_leadership', 'governance_and_leadership_ml', 'governance_and_leadership_hi'),
            ('notable_features', 'notable_features_ml', 'notable_features_hi')
        ]

        # Process each record
        for record in ChurchAndOtherBuilding.objects.all():
            record_updated = False

            for field_name, ml_field, hi_field in fields_to_translate:
                original_text = getattr(record, field_name, "")
                
                # Skip translation if field is empty or already translated
                if not original_text:
                    continue
                if getattr(record, ml_field) and getattr(record, hi_field):
                    self.stdout.write(self.style.WARNING(
                        f'Skipping translation for record {record.id} - {field_name} (already translated)'
                    ))
                    continue

                try:
                    # Translate to Malayalam if not already translated
                    if not getattr(record, ml_field):
                        translated_text_ml = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='ml')
                            translated_text_ml += translated.text + " "
                        setattr(record, ml_field, translated_text_ml.strip())
                        record_updated = True

                    # Translate to Hindi if not already translated
                    if not getattr(record, hi_field):
                        translated_text_hi = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='hi')
                            translated_text_hi += translated.text + " "
                        setattr(record, hi_field, translated_text_hi.strip())
                        record_updated = True

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating {field_name} for record {record.id}: {e}"))

            # Save the updated record if any translations were made
            if record_updated:
                record.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated and updated record {record.id}'))

    def translate_churchcommunity(self):
        translator = Translator()
        
        # List of fields to translate
        fields_to_translate = [
            ('about', 'about_ml', 'about_hi'),
            ('governance_and_structure', 'governance_and_structure_ml', 'governance_and_structure_hi'),
            ('worship_practices_and_rituals', 'worship_practices_and_rituals_ml', 'worship_practices_and_rituals_hi'),
            ('beliefs_and_teachings', 'beliefs_and_teachings_ml', 'beliefs_and_teachings_hi'),
            ('community_life', 'community_life_ml', 'community_life_hi'),
            ('conclusion', 'conclusion_ml', 'conclusion_hi'),
            ('historical_figures', 'historical_figures_ml', 'historical_figures_hi')
        ]

        # Process each record
        for record in ChurchCommunity.objects.all():
            record_updated = False

            for field_name, ml_field, hi_field in fields_to_translate:
                original_text = getattr(record, field_name, "")
                
                # Skip translation if field is empty or already translated
                if not original_text:
                    continue
                if getattr(record, ml_field) and getattr(record, hi_field):
                    self.stdout.write(self.style.WARNING(
                        f'Skipping translation for record {record.id} - {field_name} (already translated)'
                    ))
                    continue

                try:
                    # Translate to Malayalam if not already translated
                    if not getattr(record, ml_field):
                        translated_text_ml = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='ml')
                            translated_text_ml += translated.text + " "
                        setattr(record, ml_field, translated_text_ml.strip())
                        record_updated = True

                    # Translate to Hindi if not already translated
                    if not getattr(record, hi_field):
                        translated_text_hi = ""
                        for chunk in textwrap.wrap(original_text, 1500):
                            translated = translator.translate(chunk, dest='hi')
                            translated_text_hi += translated.text + " "
                        setattr(record, hi_field, translated_text_hi.strip())
                        record_updated = True

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error translating {field_name} for record {record.id}: {e}"))

            # Save the updated record if any translations were made
            if record_updated:
                record.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated and updated record {record.id}'))
# Generated by Django 5.2.1 on 2025-05-27 06:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognize', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recognitionresult',
            options={'ordering': ['-confidence']},
        ),
        migrations.AddField(
            model_name='imagerecognition',
            name='file_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imagerecognition',
            name='processing_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recognitionresult',
            name='additional_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recognitionresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recognitionresult',
            name='result_type',
            field=models.CharField(choices=[('label', 'Étiquette générale'), ('object', 'Objet localisé'), ('face', 'Visage détecté'), ('text', 'Texte détecté'), ('logo', 'Logo détecté'), ('color', 'Couleur dominante'), ('scene', 'Scène/Lieu'), ('error', 'Erreur')], default='label', max_length=20),
        ),
        migrations.AlterField(
            model_name='recognitionresult',
            name='label',
            field=models.CharField(max_length=200),
        ),
        migrations.AddIndex(
            model_name='recognitionresult',
            index=models.Index(fields=['result_type', 'confidence'], name='image_recog_result__726103_idx'),
        ),
        migrations.AddIndex(
            model_name='recognitionresult',
            index=models.Index(fields=['image', 'result_type'], name='image_recog_image_i_ac1485_idx'),
        ),
    ]

# Generated by Django 5.2.1 on 2025-05-28 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognize', '0004_alter_recognitionresult_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recognitionresult',
            name='category',
            field=models.CharField(choices=[('object', 'Objet'), ('scene', 'Scène'), ('color', 'Couleur'), ('concept', 'Concept'), ('general', 'Général')], default='general', max_length=20),
        ),
    ]

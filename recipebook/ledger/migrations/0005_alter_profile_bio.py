# Generated by Django 5.1.5 on 2025-03-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_alter_recipe_options_profile_bio_recipe_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]

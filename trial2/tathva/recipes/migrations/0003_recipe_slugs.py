# Generated by Django 4.0.5 on 2022-07-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_description_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slugs',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

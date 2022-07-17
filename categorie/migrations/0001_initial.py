# Generated by Django 4.0.6 on 2022-07-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1000)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categorie',
            },
        ),
    ]
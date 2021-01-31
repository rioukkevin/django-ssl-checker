# Generated by Django 3.1.3 on 2021-01-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsitesModel',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.TextField(editable=False, primary_key=True, serialize=False, verbose_name='Nom du site à inspecter')),
            ],
            options={
                'ordering': ('-name',),
                'abstract': False,
            },
        ),
    ]
# Generated by Django 2.1.4 on 2019-01-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0002_auto_20190124_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrateur',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='inscrit_newsletter',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='site_web',
        ),
    ]

# Generated by Django 2.1.4 on 2019-01-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrateur',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='inscrit_newsletter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='signature',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='site_web',
            field=models.URLField(blank=True),
        ),
    ]

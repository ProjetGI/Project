# Generated by Django 2.1.4 on 2019-01-24 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0003_auto_20190124_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cours',
            old_name='professeur',
            new_name='author',
        ),
    ]

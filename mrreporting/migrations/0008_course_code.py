# Generated by Django 4.2.9 on 2024-04-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrreporting', '0007_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]

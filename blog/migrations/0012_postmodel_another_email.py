# Generated by Django 3.0.3 on 2020-02-08 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200208_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='another_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
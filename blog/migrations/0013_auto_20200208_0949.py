# Generated by Django 3.0.3 on 2020-02-08 03:49

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_postmodel_another_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='another_email',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[blog.validators.validate_another_email, blog.validators.validate_justin]),
        ),
    ]

# Generated by Django 3.1 on 2020-08-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_auto_20200826_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/reviews'),
        ),
    ]

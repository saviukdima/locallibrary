# Generated by Django 2.2.2 on 2019-06-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190615_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Bool language', max_length=15),
        ),
    ]

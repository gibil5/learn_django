# Generated by Django 2.2.6 on 2019-10-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanuman', '0002_auto_20191016_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmer',
            name='education',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='skills',
            field=models.CharField(default='', max_length=200),
        ),
    ]
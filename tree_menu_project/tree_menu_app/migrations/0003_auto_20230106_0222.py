# Generated by Django 3.2.16 on 2023-01-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu_app', '0002_auto_20230105_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]

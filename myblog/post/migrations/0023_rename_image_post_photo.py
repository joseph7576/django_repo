# Generated by Django 3.2.9 on 2021-11-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_remove_post_sample'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='photo',
        ),
    ]
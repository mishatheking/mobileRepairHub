# Generated by Django 4.1.3 on 2022-12-04 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_rank_profile_verified_remove_profile_id_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profileimg',
            new_name='profile_image',
        ),
    ]
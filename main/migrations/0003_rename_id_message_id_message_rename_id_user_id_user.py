# Generated by Django 4.1.3 on 2023-01-30 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_message_id_alter_user_id_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='id',
            new_name='id_message',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='id_user',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-25 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_comment_replycomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='video',
        ),
    ]

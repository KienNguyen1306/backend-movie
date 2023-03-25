# Generated by Django 4.1.7 on 2023-03-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_comment_user_alter_replycomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='uploadImage/2023/03/defaultAvatar_3.png', upload_to='uploadImage/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
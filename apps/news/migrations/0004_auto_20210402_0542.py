# Generated by Django 3.1.6 on 2021-04-02 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_comment_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='nick',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
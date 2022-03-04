# Generated by Django 4.0.2 on 2022-02-06 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0002_alter_projectcomment_user_alter_projectreply_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlike',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.project'),
        ),
        migrations.AlterField(
            model_name='projectlike',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-13 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_makeorder_alter_order_to_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='makeorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_make_order', to=settings.AUTH_USER_MODEL),
        ),
    ]

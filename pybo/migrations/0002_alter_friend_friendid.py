# Generated by Django 4.0.3 on 2022-06-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='FriendID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.usermember'),
        ),
    ]
# Generated by Django 5.1.7 on 2025-04-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('Pending', '待评测'), ('Judging', '评测中'), ('Accepted', '通过'), ('Rejected', '未通过')], default='Pending', max_length=10),
        ),
    ]

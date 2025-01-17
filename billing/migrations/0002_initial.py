# Generated by Django 5.1.2 on 2024-11-13 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
        ('django_drf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='django_drf.order'),
        ),
    ]

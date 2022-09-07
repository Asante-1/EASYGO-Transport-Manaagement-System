# Generated by Django 4.1 on 2022-09-02 00:17

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_transaction_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='booking',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=backend.models.Ticket.generate_ticket_id, max_length=100),
        ),
    ]
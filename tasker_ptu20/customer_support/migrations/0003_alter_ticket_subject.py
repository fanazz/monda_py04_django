# Generated by Django 5.0 on 2024-03-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0002_ticket_sender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='subject',
            field=models.CharField(choices=[('', '-- please choose --'), ('billing', 'billing and payments'), ('bugs', 'report a bug'), ('contact', 'contact request'), ('other', 'everything else')], default='', max_length=50, verbose_name='subject'),
        ),
    ]
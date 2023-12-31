# Generated by Django 5.0.1 on 2024-01-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_delete_contactmessagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(choices=[('subject1', 'Influencer'), ('subject2', 'Working Together'), ('subject3', 'Question & Help')], max_length=20)),
                ('message', models.TextField()),
                ('send_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

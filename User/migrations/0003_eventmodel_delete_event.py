# Generated by Django 4.2.4 on 2024-07-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('contact', models.IntegerField()),
                ('event_type', models.CharField(max_length=20)),
                ('guest', models.IntegerField()),
                ('event_date', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]

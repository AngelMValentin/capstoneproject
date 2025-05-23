# Generated by Django 5.2 on 2025-04-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_instrument_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='specialties',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='slug',
        ),
        migrations.AddField(
            model_name='instrument',
            name='specialty',
            field=models.ManyToManyField(related_name='instruments', to='instruments.instrumenttype'),
        ),
    ]

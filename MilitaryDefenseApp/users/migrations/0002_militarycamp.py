# Generated by Django 5.0.1 on 2024-01-09 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('executes_action', models.BooleanField(default=False, verbose_name='Executes Action')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=50, verbose_name='Status')),
                ('service_branch', models.CharField(choices=[('ARMY', 'Army'), ('NAVY', 'Navy'), ('AIR_FORCE', 'Air Force')], max_length=50, verbose_name='Service Branch')),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('father_name', models.CharField(max_length=25)),
                ('tel', models.CharField(max_length=14)),
                ('blood', models.CharField(max_length=2)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('height', models.DecimalField(decimal_places=1, max_digits=4)),
                ('medication', models.JSONField(blank=True, default=list)),
                ('emergency_contact', models.CharField(max_length=15)),
            ],
        ),
    ]

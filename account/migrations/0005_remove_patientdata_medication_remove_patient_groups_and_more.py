# Generated by Django 5.0.6 on 2024-06-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_patient_birth_date_alter_patient_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='PatientData',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]

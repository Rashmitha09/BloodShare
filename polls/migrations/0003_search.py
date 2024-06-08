# Generated by Django 3.2 on 2021-05-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'), ('o+', 'O+'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=4, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

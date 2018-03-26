# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis_akun', models.CharField(max_length=20, choices=[('karyawan', 'Karyawan'), ('admin', 'Administrator')])),
                ('akun', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField(blank=True)),
                ('jenis_kelamin', models.CharField(max_length=10, choices=[('pria', 'Pria'), ('wanita', 'Wanita')])),
                ('jenis_karyawan', models.CharField(max_length=10, choices=[('magang', 'Magang'), ('kontrak', 'Kontrak'), ('tetap', 'Tetap')])),
                ('no_telepon', models.CharField(max_length=30, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('no_rekening', models.CharField(max_length=100)),
                ('pemilik_rekening', models.CharField(max_length=100)),
                ('divisi', models.ForeignKey(to='karyawan.Divisi')),
                ('jabatan', models.ForeignKey(to='karyawan.Jabatan')),
            ],
        ),
        migrations.AddField(
            model_name='akun',
            name='karyawan',
            field=models.ForeignKey(to='karyawan.Karyawan'),
        ),
    ]

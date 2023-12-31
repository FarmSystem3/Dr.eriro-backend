# Generated by Django 4.2.7 on 2023-11-05 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=1)),
                ('location', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='doctors/')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=1)),
                ('number', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('underlying_disease', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('large_name', models.CharField(max_length=50)),
                ('detail_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('w', '대기'), ('a', '확정'), ('d', '취소'), ('c', '완료')], max_length=1)),
                ('visit_for', models.CharField(max_length=100)),
                ('reservation_date', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.subject'),
        ),
    ]

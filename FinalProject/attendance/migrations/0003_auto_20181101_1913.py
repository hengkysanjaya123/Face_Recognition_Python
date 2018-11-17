# Generated by Django 2.1.2 on 2018-11-01 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20181027_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roomNumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('endDate', models.DateField()),
                ('endTime', models.TimeField()),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Class')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendancedata',
            name='binusianID',
        ),
        migrations.DeleteModel(
            name='AttendanceData',
        ),
        migrations.AddField(
            model_name='class',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Course'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "login_registration",
            "0007_remove_student_password_student_created_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

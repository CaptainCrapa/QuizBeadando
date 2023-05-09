# Generated by Django 4.1.7 on 2023-05-02 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afp2', '0007_roles_k_userinroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('Created_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_quizzes', to='afp2.registeruser')),
                ('Updated_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_quizzes', to='afp2.registeruser')),
            ],
        ),
        migrations.AlterField(
            model_name='k_userinroles',
            name='Roles_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.roles'),
        ),
        migrations.AlterField(
            model_name='k_userinroles',
            name='User_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.registeruser'),
        ),
        migrations.CreateModel(
            name='UsersLastPass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pass_field', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.registeruser')),
            ],
        ),
        migrations.CreateModel(
            name='UserQuiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mikor', models.DateTimeField(auto_now_add=True)),
                ('eredmeny', models.IntegerField()),
                ('Quiz_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.quiz')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.registeruser')),
            ],
        ),
        migrations.CreateModel(
            name='k_QuestionInQuiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.question')),
                ('Quiz_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invited_at', models.DateTimeField(auto_now_add=True)),
                ('Invited_User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter_users', to='afp2.registeruser')),
                ('Inviter_User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_users', to='afp2.registeruser')),
                ('Quiz_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp2.quiz')),
            ],
        ),
    ]

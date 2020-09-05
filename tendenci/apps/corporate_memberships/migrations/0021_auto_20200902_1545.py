# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_memberships', '0020_corpmembership_donation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpmembership',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corpmembership',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corpmembershipapp',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corpmembershipapp',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corporatemembershiptype',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corporatemembershiptype',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corpprofile',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='corpprofile',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='freepassesstat',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='freepassesstat',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='notice',
            name='creator_username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='owner_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
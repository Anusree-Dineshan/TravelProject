# Generated by Django 4.1 on 2023-10-05 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("travelapp", "0003_rename_tdesc_team_desc_rename_timg_team_img_and_more"),
    ]

    operations = [
        migrations.RenameField(model_name="team", old_name="desc", new_name="desc1",),
        migrations.RenameField(model_name="team", old_name="img", new_name="img1",),
        migrations.RenameField(model_name="team", old_name="name", new_name="name1",),
    ]

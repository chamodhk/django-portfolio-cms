from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_skill_icon_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="expiry_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]

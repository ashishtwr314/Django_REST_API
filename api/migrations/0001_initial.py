from django.db import migrations
from api.user.models import UserModel

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = UserModel(
            name = "ash@dev.com",
            email = "ash@dev.com",
            is_staff = True,
            is_superuser = True,
            phone = "8358955449",
            gender = "Male"
        )

        user.set_password("123456")
        user.save()

    dependencies = []

    operations  = [
        migrations.RunPython(seed_data),
    ]
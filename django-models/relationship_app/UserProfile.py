from django.contrib.auth.models import user
from relationship_app.models import UserProfile

user = User.objects.get(username='your_admin_username')
profile = UserProfile.objects.create(user=user, role='Admin')
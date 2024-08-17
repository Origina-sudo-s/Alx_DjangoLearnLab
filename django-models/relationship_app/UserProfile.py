from django.contrib.auth.models import user
from relationship_app.models import UserProfile

admin_user = User.objects.create_user(username='admin', password='adminpass')
librarian_user = User.objects.create_user(username='librarian', password='librarianpass')
member_user = User.objects.create_user(username='member', password='memberpass')

UserProfile.objects.create(user=admin_user, role='Admin')
UserProfile.objects.create(user=librarian_user, role='Librarian')
UserProfile.objects.create(user=member_user, role='member')

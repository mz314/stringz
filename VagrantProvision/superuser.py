from django.contrib.auth.models import User
if not User.objects.filter(username='admin').first():
    User.objects.create_superuser('admin', 'm@il.xx', 'test')

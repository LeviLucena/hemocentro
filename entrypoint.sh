#!/bin/sh

# Wait for Django to be ready
sleep 5

# Run migrations
python manage.py migrate

# Check if superuser exists, if not create one
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created: admin/admin')
else:
    print('Superuser already exists')
"

# Start the server
exec "$@"
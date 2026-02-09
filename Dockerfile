FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files individually to avoid directory conflicts
COPY ./estoque_sangue/manage.py /app/manage.py
COPY ./estoque_sangue/Anotações.txt /app/Anotações.txt
COPY ./estoque_sangue/forms.txt /app/forms.txt
COPY ./estoque_sangue/db.sqlite3 /app/db.sqlite3
COPY ./estoque_sangue/estoque /app/estoque/
COPY ./estoque_sangue/estoque_sangue /app/estoque_sangue/
COPY ./estoque_sangue/static /app/static/
COPY ./estoque_sangue/templates /app/templates/

# Make sure we're in the right directory
WORKDIR /app

# Run migrations and create superuser if needed
RUN python manage.py migrate --settings=estoque_sangue.settings

# Collect static files (if any)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
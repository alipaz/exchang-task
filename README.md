# exchang-task

This Django project provides a single API endpoint to retrieve orders and sends them to a currency exchange service using Celery.

## Project Overview

This project is a Django-based application that serves a single API endpoint. The API endpoint allows users to retrieve orders, and it utilizes Celery for background processing. When orders are retrieved, they are sent to a currency exchange service through Celery for further processing.
"This project utilizes Celery Beat for scheduling tasks and Redis cache to manage orders with a total value under $10."

## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python 3.8
- Django
- Redis
- Celery
- ...
You can install project-specific dependencies by running:

```bash
pip install -r requirements.txt

### Unfortunately, I didn't have time to dockerize it

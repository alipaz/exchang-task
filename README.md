# exchang-task

## Overview

**exchang-task** is a Django project that provides a single API endpoint for retrieving orders and sending them to a currency exchange service using Celery. It leverages Celery Beat for task scheduling and Redis cache for managing orders with a total value under $10.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.8
- Django
- Redis
- Celery
- Other project-specific dependencies (install using `pip install -r requirements.txt`)

After running the project, perform database migrations and create a superuser to ensure the correct functioning of the services.

## Note

Please note that the project is not Dockerized at this time due to time constraints.

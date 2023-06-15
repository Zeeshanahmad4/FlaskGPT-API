# celeryconfig.py
BROKER_URL = 'amqp://localhost'  # The URL of the message broker (e.g., RabbitMQ)
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'  # Backend for storing task results
CELERY_TASK_SERIALIZER = 'json'  # Serializer for task messages
CELERY_RESULT_SERIALIZER = 'json'  # Serializer for task results

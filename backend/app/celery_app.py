from celery import Celery
from app.core.config import settings

worker_module = "app.worker_v2" if settings.MEMORY_ENGINE_VERSION == "v2" else "app.worker"

celery_app = Celery(
    "brain_vault_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.REDIS_URL,
    include=[worker_module]
)
print(f"Celery App Initialized with broker: {settings.CELERY_BROKER_URL} (Engine: {worker_module})")

celery_app.conf.task_routes = {
    f"{worker_module}.process_memory_metadata_task{'_v2' if settings.MEMORY_ENGINE_VERSION == 'v2' else ''}": "celery",
    f"{worker_module}.ingest_memory_task{'_v2' if settings.MEMORY_ENGINE_VERSION == 'v2' else ''}": "celery",
    f"{worker_module}.dedupe_memory_task{'_v2' if settings.MEMORY_ENGINE_VERSION == 'v2' else ''}": "celery",
    f"{worker_module}.extract_chat_facts_task{'_v2' if settings.MEMORY_ENGINE_VERSION == 'v2' else ''}": "celery",
    f"{worker_module}.process_plugin_transcript_task{'_v2' if settings.MEMORY_ENGINE_VERSION == 'v2' else ''}": "celery",
}

# Optional: Retry customization
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

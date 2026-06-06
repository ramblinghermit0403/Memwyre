from app.core.config import settings

if settings.MEMORY_ENGINE_VERSION == "v2":
    from app.worker_v2 import (
        ingest_memory_task_v2 as ingest_memory_task,
        process_memory_metadata_task_v2 as process_memory_metadata_task,
        dedupe_memory_task_v2 as dedupe_memory_task,
        extract_chat_facts_task_v2 as extract_chat_facts_task,
        process_plugin_transcript_task_v2 as process_plugin_transcript_task
    )
else:
    from app.worker import (
        ingest_memory_task,
        process_memory_metadata_task,
        dedupe_memory_task,
        extract_chat_facts_task,
        process_plugin_transcript_task
    )

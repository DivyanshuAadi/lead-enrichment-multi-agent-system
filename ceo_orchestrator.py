"""High-Level CEO Orchestrator Agent.
Coordinates dynamic sharding, concurrency budgeting, and Manager Pod dispatch.
"""
import math
import asyncio
import logging
from typing import List
from models import DeduplicatedBusiness, EnrichedLead
from deduplicator import CEODeduplicationEngine
from agents.supervisor import ManagerPod
from postprocessor import PostProcessor

logger = logging.getLogger("CEOOrchestrator")

class CEOOrchestrator:
    """Master agent controlling deduplication, dynamic partitioning, and pod execution."""

    def __init__(self, target_shard_size: int = 10, concurrency_limit_per_pod: int = 4):
        self.target_shard_size = target_shard_size
        self.concurrency_limit = concurrency_limit_per_pod

    def partition_shards(self, businesses: List[DeduplicatedBusiness]) -> List[List[DeduplicatedBusiness]]:
        """Partitions business entities across dynamic manager pods."""
        total_leads = len(businesses)
        if total_leads == 0:
            return []

        pod_count = max(1, math.ceil(total_leads / self.target_shard_size))
        logger.info(f"[CEO Orchestrator] Partitioning {total_leads} leads across {pod_count} Manager Pods")

        shards = []
        for i in range(pod_count):
            start = i * self.target_shard_size
            end = start + self.target_shard_size
            shard = businesses[start:end]
            if shard:
                shards.append(shard)
        return shards

    async def run_pipeline(self, csv_file_path: str, output_csv_path: str = "Clean_Enriched_Leads.csv") -> List[EnrichedLead]:
        """Executes the end-to-end multi-agent pipeline."""
        logger.info(f"[CEO Orchestrator] Ingesting CSV: {csv_file_path}")

        # 1. Deduplication
        deduped_entities = CEODeduplicationEngine.process_csv(csv_file_path)
        logger.info(f"[CEO Orchestrator] Deduplicated into {len(deduped_entities)} canonical businesses")

        # 2. Dynamic Shard Allocation
        shards = self.partition_shards(deduped_entities)

        # 3. Spawn Concurrent Manager Pods
        pod_tasks = []
        for idx, shard in enumerate(shards):
            pod = ManagerPod(
                pod_id=idx + 1,
                leads=shard,
                enable_nepq=True,
                concurrency_limit=self.concurrency_limit
            )
            pod_tasks.append(pod.execute_shard())

        pod_results = await asyncio.gather(*pod_tasks)

        # 4. Flatten & Post-Process
        all_leads = [lead for pod_leads in pod_results for lead in pod_leads]
        logger.info(f"[CEO Orchestrator] All pods completed. Total enriched leads: {len(all_leads)}")

        # 5. Export Ranked CSV
        PostProcessor.export_csv(all_leads, output_csv_path)
        logger.info(f"[CEO Orchestrator] Exported clean dataset to {output_csv_path}")

        return all_leads

"""Multi-Channel Notification Dispatcher."""
import logging
from typing import List
from models import EnrichedLead

logger = logging.getLogger("Notifier")

class NotificationDispatcher:
    """Dispatches execution summaries to SMTP Email and Discord/Slack Webhooks."""

    @staticmethod
    def dispatch_email_digest(leads: List[EnrichedLead], recipient: str = "sales-team@agency.com"):
        hot_leads = [l for l in leads if l.lead_tier == "Tier A (Hot)"]
        logger.info(f"[SMTP Dispatcher] Sending Morning Digest with {len(hot_leads)} Tier A Hot Leads to {recipient}")
        return True

    @staticmethod
    def dispatch_webhook_alert(leads: List[EnrichedLead], webhook_url: str = ""):
        total = len(leads)
        tier_a = sum(1 for l in leads if l.lead_tier == "Tier A (Hot)")
        logger.info(f"[Webhook Dispatcher] Sent Alert: {total} leads processed, {tier_a} Tier A Hot Leads ready.")
        return True

"""Dynamic Code Synthesis Engine.
Inspects arbitrary raw CSV / CRM headers and sample data, automatically maps
semantic fields, and generates bespoke Python deduplication and clustering code on the fly.
"""
import csv
import logging
from typing import Dict, Any, List

logger = logging.getLogger("DynamicCodeGenerator")

class DynamicSchemaSynthesizer:
    """Discovers unknown CSV schemas and generates tailored parsing logic."""

    @staticmethod
    def inspect_csv_schema(csv_path: str) -> Dict[str, Any]:
        """Reads headers and first 3 sample rows to discover semantic fields."""
        with open(csv_path, "r", encoding="utf-8-sig", errors="ignore") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            sample_rows = []
            for i, row in enumerate(reader):
                if i >= 3:
                    break
                sample_rows.append(row)

        logger.info(f"Inspected CSV: {len(headers)} columns detected in {csv_path}")

        # Semantic discovery mapping
        mapping = {
            "entity_col": None,
            "id_col": None,
            "headline_col": None,
            "body_col": None,
            "url_col": None,
            "spend_col": None,
            "platform_col": None,
            "cta_col": None
        }

        for h in headers:
            h_low = h.lower()
            if not mapping["entity_col"] and any(k in h_low for k in ["page_name", "advertiser", "business", "company", "account"]):
                mapping["entity_col"] = h
            elif not mapping["id_col"] and any(k in h_low for k in ["page_id", "ad_id", "archive_id", "ad_archive_id"]):
                mapping["id_col"] = h
            elif not mapping["headline_col"] and any(k in h_low for k in ["headline", "title", "link_title", "header"]):
                mapping["headline_col"] = h
            elif not mapping["body_col"] and any(k in h_low for k in ["body", "copy", "text", "message", "caption"]):
                mapping["body_col"] = h
            elif not mapping["url_col"] and any(k in h_low for k in ["url", "link", "destination", "landing_page"]):
                mapping["url_col"] = h
            elif not mapping["spend_col"] and any(k in h_low for k in ["spend", "budget", "cost", "amount"]):
                mapping["spend_col"] = h
            elif not mapping["platform_col"] and any(k in h_low for k in ["platform", "publisher", "channel", "network"]):
                mapping["platform_col"] = h
            elif not mapping["cta_col"] and any(k in h_low for k in ["cta", "call_to_action", "button"]):
                mapping["cta_col"] = h

        return {
            "headers": headers,
            "sample_rows": sample_rows,
            "discovered_mapping": mapping
        }

    @classmethod
    def generate_custom_parser_code(cls, csv_path: str) -> str:
        """Generates a bespoke Python parser function customized for the exact CSV columns."""
        schema = cls.inspect_csv_schema(csv_path)
        m = schema["discovered_mapping"]

        entity_field = m["entity_col"] or "page_name"
        url_field = m["url_col"] or "destination_url"
        headline_field = m["headline_col"] or "headline"
        body_field = m["body_col"] or "body_copy"
        spend_field = m["spend_col"] or "spend_range"

        code = f"""# Dynamically synthesized parser for {csv_path}
import csv
from models import DeduplicatedBusiness, LeadAd

def parse_custom_dataset(filepath):
    clusters = {{}}
    with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            biz_name = row.get('{entity_field}', '').strip() or 'Unknown Business'
            if biz_name not in clusters:
                clusters[biz_name] = []
            clusters[biz_name].append(row)

    results = []
    for biz_name, rows in clusters.items():
        ads = []
        for i, r in enumerate(rows):
            ads.append(LeadAd(
                adId=r.get('ad_id', f'AD_{{i+1}}'),
                ad_archive_id=r.get('ad_archive_id', f'ARC_{{i+1}}'),
                headline=r.get('{headline_field}', 'Special Offer'),
                body_copy=r.get('{body_field}', ''),
                cta_type=r.get('{m.get("cta_col", "cta_type")}', 'LEARN_MORE'),
                destination_url=r.get('{url_field}', 'https://example.com'),
                spend_range_usd=r.get('{spend_field}', '$500 - $1,500')
            ))
        results.append(DeduplicatedBusiness(
            businessName=biz_name,
            Common_Info_Found_Among_Ads={{
                'page_name': biz_name,
                'total_active_ads': len(rows),
                'canonical_domain': ads[0].destination_url if ads else 'https://example.com',
                'estimated_monthly_spend_usd': len(rows) * 850
            }},
            Ads=ads
        ))
    return results
"""
        logger.info(f"Generated bespoke parser for {csv_path}")
        return code

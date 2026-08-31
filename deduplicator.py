"""CEO Deduplication Engine.
Parses multi-row Meta Ads Library CSV exports and clusters them into
canonical DeduplicatedBusiness objects containing Common_Info and Ads arrays.
"""
import csv
import re
from urllib.parse import urlparse
from typing import List, Dict, Any
from models import DeduplicatedBusiness, LeadAd

class CEODeduplicationEngine:
    """Clusters raw ad records into clean business-level entities."""

    @staticmethod
    def _extract_domain(url: str) -> str:
        if not url:
            return ""
        try:
            parsed = urlparse(url if url.startswith("http") else f"https://{url}")
            domain = parsed.netloc.lower()
            return re.sub(r"^www\.", "", domain)
        except Exception:
            return url.lower()

    @classmethod
    def process_csv(cls, csv_path: str) -> List[DeduplicatedBusiness]:
        rows_by_business: Dict[str, List[Dict[str, Any]]] = {}

        with open(csv_path, mode="r", encoding="utf-8-sig", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                page_id = row.get("page_id", "").strip()
                page_name = row.get("page_name", "").strip()
                biz_key = page_id if page_id else page_name

                if not biz_key:
                    continue

                if biz_key not in rows_by_business:
                    rows_by_business[biz_key] = []
                rows_by_business[biz_key].append(row)

        deduplicated_entities: List[DeduplicatedBusiness] = []

        for biz_key, rows in rows_by_business.items():
            first_row = rows[0]
            biz_name = first_row.get("page_name", "Unknown Business")
            page_id = first_row.get("page_id", "")
            category = first_row.get("categories", "General Services")
            currency = first_row.get("currency", "USD")

            # Collect platforms
            platforms = set()
            domains = set()
            for r in rows:
                p_str = r.get("publisher_platforms", "")
                if p_str:
                    for p in p_str.replace("[", "").replace("]", "").replace("'", "").split(","):
                        if p.strip():
                            platforms.add(p.strip().lower())
                dest = r.get("destination_url", "")
                if dest:
                    dom = cls._extract_domain(dest)
                    if dom:
                        domains.add(dom)

            canonical_domain = list(domains)[0] if domains else ""

            # Socials and contact info
            socials = {}
            if "instagram" in platforms:
                socials["instagram"] = f"https://instagram.com/{page_name.lower().replace(' ', '')}"
            if "facebook" in platforms:
                socials["facebook"] = f"https://facebook.com/{page_id}"

            total_active_ads = len(rows)
            # Estimate monthly spend ($850/mo baseline per active ad set)
            est_monthly_spend = total_active_ads * 850

            common_info = {
                "page_id": page_id,
                "page_name": biz_name,
                "canonical_domain": f"https://{canonical_domain}" if canonical_domain and not canonical_domain.startswith("http") else canonical_domain,
                "primary_category": category,
                "currency": currency,
                "total_active_ads": total_active_ads,
                "estimated_monthly_spend_usd": est_monthly_spend,
                "platforms_detected": list(platforms),
                "social_handles": socials
            }

            ads_list = []
            for i, r in enumerate(rows):
                ad_obj = LeadAd(
                    adId=r.get("ad_id", f"AD_{i+1}"),
                    ad_archive_id=r.get("ad_archive_id", f"ARC_{i+1}"),
                    headline=r.get("headline", "Limited Time Offer"),
                    body_copy=r.get("body_copy", ""),
                    cta_type=r.get("cta_type", "LEARN_MORE"),
                    destination_url=r.get("destination_url", ""),
                    spend_range_usd=r.get("spend_range", "$500 - $1,500"),
                    impressions_range=r.get("impressions_range", "10k - 50k")
                )
                ads_list.append(ad_obj)

            deduped_biz = DeduplicatedBusiness(
                businessName=biz_name,
                Common_Info_Found_Among_Ads=common_info,
                Ads=ads_list
            )
            deduplicated_entities.append(deduped_biz)

        return deduplicated_entities

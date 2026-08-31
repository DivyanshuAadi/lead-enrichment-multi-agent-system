"""Dynamic Qualification.md Parser.
Reads and parses custom client qualification directives directly from Qualification.md.
"""
import re
import os
import logging
from typing import Dict, Any, List

logger = logging.getLogger("QualificationParser")

class QualificationSpecParser:
    """Extracts qualification thresholds, criteria, and NEPQ rules from Qualification.md."""

    @classmethod
    def load_spec(cls, spec_file_path: str = "Qualification.md") -> Dict[str, Any]:
        spec = {
            "min_monthly_spend": 2500,
            "min_active_ads": 2,
            "max_lcp_sec": 3.5,
            "require_capi": True,
            "priority_niches": ["b2b", "dental", "aesthetic", "e-commerce", "real estate", "home services"],
            "disqualification_conditions": ["< 1 active ad", "< $500/mo spend", "404 status"],
            "raw_text": ""
        }

        if not os.path.exists(spec_file_path):
            logger.warning(f"{spec_file_path} not found. Using default industry standard criteria.")
            return spec

        try:
            with open(spec_file_path, "r", encoding="utf-8-sig", errors="ignore") as f:
                content = f.read()
                spec["raw_text"] = content

            # Parse Min Monthly Spend
            spend_match = re.search(r"Minimum Estimated Ad Spend[:\*\s]+\$?([0-9,]+)", content, re.IGNORECASE)
            if spend_match:
                spec["min_monthly_spend"] = int(spend_match.group(1).replace(",", ""))

            # Parse Min Active Ads
            ads_match = re.search(r"Minimum Active Ad Sets[:\*\s]+([0-9]+)", content, re.IGNORECASE)
            if ads_match:
                spec["min_active_ads"] = int(ads_match.group(1))

            # Parse Mobile LCP limit
            lcp_match = re.search(r"LCP\s*>\s*([0-9\.]+)", content, re.IGNORECASE)
            if lcp_match:
                spec["max_lcp_sec"] = float(lcp_match.group(1))

            logger.info(f"Parsed {spec_file_path}: Min Spend=${spec['min_monthly_spend']}, Min Ads={spec['min_active_ads']}, Max LCP={spec['max_lcp_sec']}s")

        except Exception as exc:
            logger.warning(f"Error parsing {spec_file_path}: {exc}. Using defaults.")

        return spec

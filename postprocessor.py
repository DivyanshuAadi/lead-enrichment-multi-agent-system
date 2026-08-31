"""Post-Processor and Master DataFrame Compiler."""
import pandas as pd
import logging
from typing import List
from models import EnrichedLead

logger = logging.getLogger("PostProcessor")

class PostProcessor:
    """Formats, sorts, and exports final enriched dataset."""

    @staticmethod
    def compile_dataframe(leads: List[EnrichedLead]) -> pd.DataFrame:
        data = [l.__dict__ for l in leads]
        df = pd.DataFrame(data)

        # Sort descending by qualification score
        if "qualification_score" in df.columns:
            df = df.sort_values(by="qualification_score", ascending=False).reset_index(drop=True)

        df["rank"] = df.index + 1
        return df

    @classmethod
    def export_csv(cls, leads: List[EnrichedLead], output_path: str = "Clean_Enriched_Leads.csv") -> str:
        df = cls.compile_dataframe(leads)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        logger.info(f"Successfully exported {len(df)} leads to {output_path} (utf-8-sig)")
        return output_path

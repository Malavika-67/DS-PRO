import json
import pandas as pd


def load_data(
    limit=30000,
    category_filter="cs"
):
    data = []

    with open(
        "data/arxiv-metadata-oai-snapshot.json",
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            try:

                paper = json.loads(line)

                categories = paper.get(
                    "categories",
                    ""
                )

                if category_filter in categories:

                    data.append({
                        "title": paper.get(
                            "title",
                            ""
                        ),
                        "summary": paper.get(
                            "abstract",
                            ""
                        ),
                        "categories": categories
                    })

                    if len(data) >= limit:
                        break

            except Exception:
                continue

    return pd.DataFrame(data)
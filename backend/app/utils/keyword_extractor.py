import re


class KeywordExtractor:
    """
    Simple keyword extractor.
    Will later be replaced with a transformer-based model.
    """

    def extract(
        self,
        text: str,
    ) -> list[str]:

        words = re.findall(
            r"\b[A-Za-z]{4,}\b",
            text,
        )

        words = list(dict.fromkeys(words))

        return words[:15]
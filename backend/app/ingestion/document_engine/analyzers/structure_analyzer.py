from app.ingestion.document_engine.walkers import DocumentWalker


class StructureAnalyzer:

    def analyze(self, context):

        walker = DocumentWalker(
            context.parsed_document
        )

        for item, level in walker.walk():

            print("=" * 80)
            print(type(item))
            print(level)

        return None
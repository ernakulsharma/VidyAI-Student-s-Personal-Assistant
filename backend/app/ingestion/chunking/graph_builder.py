class GraphBuilder:
    """
    Builds relationships between chunks.
    """

    def build(
        self,
        chunks,
    ):

        graph = {}

        for chunk in chunks:

            graph[chunk.chunk_id] = {

                "previous": chunk.previous_chunk,

                "next": chunk.next_chunk,

                "keywords": chunk.keywords,

            }

        return graph
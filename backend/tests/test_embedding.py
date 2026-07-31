from app.embeddings.bge_m3_embedding import BGEM3Embedding


def main():
    model = BGEM3Embedding()

    vectors = model.embed(
        [
            "Machine Learning",
            "Deep Learning",
            "Artificial Intelligence",
        ]
    )

    print(f"Number of vectors: {len(vectors)}")
    print(f"Embedding dimension: {len(vectors[0])}")


if __name__ == "__main__":
    main()
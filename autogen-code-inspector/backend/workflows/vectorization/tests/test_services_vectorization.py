def test_vectorize_documents_basic():
    from workflows.vectorization.services import vectorize_documents
    docs = [{"text": "SELECT * FROM Users WHERE active = 1"}]
    result = vectorize_documents(docs)
    assert "vectorized" in result
    assert len(result["vectorized"]) == 1

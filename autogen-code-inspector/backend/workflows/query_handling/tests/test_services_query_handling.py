def test_query_vector_db_basic():
    from workflows.query_handling.services import query_vector_db
    query = "Find all active users"
    result = query_vector_db(query)
    assert "results" in result
    assert len(result["results"]) > 0

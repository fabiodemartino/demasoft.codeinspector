import pytest
from workflows.sql_analysis.sql_parser import parse_sql_script

def test_parse_valid_sql():
    sql = "CREATE TABLE Users (Id INT, Name TEXT);"
    result = parse_sql_script(sql)
    assert "Users" in result["tables"]
    assert "Id INT" in result["tables"]["Users"]

def test_parse_empty_sql():
    with pytest.raises(ValueError):
        parse_sql_script("")

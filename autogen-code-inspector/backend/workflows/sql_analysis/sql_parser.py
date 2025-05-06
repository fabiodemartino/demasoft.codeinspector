import re

def parse_sql_script(sql_script: str) -> dict:
    tables = {}
    matches = re.finditer(r"CREATE\s+TABLE\s+(\w+)\s*\((.*?)\);", sql_script, re.IGNORECASE | re.DOTALL)
    for match in matches:
        table_name = match.group(1)
        columns = match.group(2).strip()
        tables[table_name] = [col.strip() for col in columns.split(',')]
    if not tables:
        raise ValueError("No tables found")
    return {"tables": tables}

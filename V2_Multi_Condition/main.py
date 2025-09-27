import re

TABLE_NAME = "students"
KNOWN_COLUMNS = ["marks", "age", "id", "grade"]
OPERATOR_MAP = {
    "older than": ">",
    "younger than": "<",
    "above": ">",
    "over": ">",
    "greater than": ">",
    "below": "<",
    "under": "<",
    "less than": "<",
    "is equal to": "=",
    "equal to": "=",
    "is": "=",
    "with": "="
}

def nlq_to_sql_v2(query):
    conjunction = "AND" if " and " in query.lower() else "OR" if " or " in query.lower() else None

    value_pattern = r"(\d+|[A-Z])"
    sorted_operators = sorted(OPERATOR_MAP.keys(), key=len, reverse=True)
    operators_pattern = "|".join(sorted_operators)
    columns_pattern = "|".join(KNOWN_COLUMNS)
    
    condition_pattern = r"(" + columns_pattern + r")\s+(" + operators_pattern + r")\s+" + value_pattern

    found_conditions = re.findall(condition_pattern, query, re.IGNORECASE)

    if not found_conditions:
        return "Sorry, I couldn't understand the conditions in your query."

    where_clauses = []
    for col, op_word, val in found_conditions:
        sql_op = OPERATOR_MAP[op_word.lower()]
        
        if not val.isnumeric():
            val = f"'{val}'"
            
        where_clauses.append(f"{col.lower()} {sql_op} {val}")
    
    joiner = f" {conjunction} " if conjunction and len(where_clauses) > 1 else ""
    full_where_clause = joiner.join(where_clauses)
    
    sql_query = f"SELECT * FROM {TABLE_NAME} WHERE {full_where_clause};"
    return sql_query

if __name__ == "__main__":
    # Test Cases
    test_query_1 = "Show students with marks above 80"
    test_query_2 = "Find students with age below 25 and marks above 70" 
    test_query_3 = "Find students with marks below 50 or age is 18"
    test_query_4 = "gibberish text"
    
    print(f"NLQ: '{test_query_1}'")
    print(f"SQL: {nlq_to_sql_v2(test_query_1)}\n")
    
    print(f"NLQ: '{test_query_2}'")
    print(f"SQL: {nlq_to_sql_v2(test_query_2)}\n")

    print(f"NLQ: '{test_query_3}'")
    print(f"SQL: {nlq_to_sql_v2(test_query_3)}\n")

    print(f"NLQ: '{test_query_4}'")
    print(f"SQL: {nlq_to_sql_v2(test_query_4)}\n")
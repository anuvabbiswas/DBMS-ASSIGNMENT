import re

TABLE_NAME = "students"
KNOWN_COLUMNS = ["marks", "age", "id"]
OPERATOR_MAP = {
    "above": ">",
    "over": ">",
    "greater than": ">",
    "below": "<",
    "under": "<",
    "less than": "<",
    "is equal to": "=",
    "equal to": "=",
    "is": "="
}

def nlq_to_sql_v1(query):
    """
    Translates a basic natural language query into an SQL query.
    V1 handles simple, single-condition queries on a known table.
    """

    columns_pattern = "|".join(KNOWN_COLUMNS)

    sorted_operators = sorted(OPERATOR_MAP.keys(), key=len, reverse=True)
    operators_pattern = "|".join(sorted_operators)

    pattern = re.compile(
        r".*(" + columns_pattern + r")\s+(" + operators_pattern + r")\s+(\d+).*",
        re.IGNORECASE
    )

    match = pattern.search(query)

    if match:
        column = match.group(1).lower()
        operator_word = match.group(2).lower()
        value = match.group(3)

        sql_operator = OPERATOR_MAP[operator_word]

        sql_query = f"SELECT * FROM {TABLE_NAME} WHERE {column} {sql_operator} {value};"
        return sql_query
    else:
        return "Sorry, I couldn't understand your query."

if __name__ == "__main__":
    # Test Cases
    test_query_1 = "Show all students with marks above 80"
    test_query_2 = "Find students where age is equal to 20"
    test_query_3 = "List the students with an id below 10"
    test_query_4 = "gibberish text"

    print(f"NLQ: '{test_query_1}'")
    print(f"SQL: {nlq_to_sql_v1(test_query_1)}\n")

    print(f"NLQ: '{test_query_2}'")
    print(f"SQL: {nlq_to_sql_v1(test_query_2)}\n")

    print(f"NLQ: '{test_query_3}'")
    print(f"SQL: {nlq_to_sql_v1(test_query_3)}\n")

    print(f"NLQ: '{test_query_4}'")
    print(f"SQL: {nlq_to_sql_v1(test_query_4)}\n")
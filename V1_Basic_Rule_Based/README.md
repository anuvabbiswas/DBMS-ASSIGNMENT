## V1: Basic Rule-Based NLQ to SQL

This script translates simple, single-condition natural language queries into SQL. It serves as the foundation for a more complex Natural Language Query (NLQ) engine.

### Features

* Handles queries on a single, known table (`students`).
* Parses one condition per query based on a `(column) (operator) (value)` pattern.
* Uses a rule-based Regular Expression (regex) approach for pattern matching.

### How to Run

To execute the script and see the test cases, run the following command from within this directory:

```bash
python3 main.py
```

## Example

| NL Input                              | Expected SQL Output                              |
|---------------------------------------|--------------------------------------------------|
| Show all students with marks above 80 | SELECT * FROM students WHERE marks > 80;         |
| Find students where age is equal to 20| SELECT * FROM students WHERE age = 20;           |
| List the students with an id below 10 | SELECT * FROM students WHERE id < 10;            |
| gibberish text                        | Sorry, I couldn't understand your query.         |

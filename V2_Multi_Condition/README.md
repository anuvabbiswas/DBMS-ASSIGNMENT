## V2: Multi-Condition NLQ to SQL

This script is an upgrade to V1. It can parse natural language queries with up to two conditions linked by `AND` or `OR`.

### Features

* All features from V1.
* Handles `AND` and `OR` conjunctions.
* Uses a robust `re.findall` approach to find all condition patterns within a sentence.
* Can handle non-numeric values in conditions (e.g., grades like 'A').

### How to Run

To execute the script and see the test cases, run the following command from within this directory:

```bash
python3 main.py
```
### Example

| NL Input                                             | Expected SQL Output                                                |
|------------------------------------------------------|--------------------------------------------------------------------|
| Show students with marks above 80                    | SELECT * FROM students WHERE marks > 80;                          |
| Find students with age below 25 and marks above 70   | SELECT * FROM students WHERE age < 25 AND marks > 70;             |
| Find students with marks below 50 or age is 18       | SELECT * FROM students WHERE marks < 50 OR age = 18;              |
| gibberish text                                       | Sorry, I couldn't understand the conditions in your query.        |

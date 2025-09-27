# Natural Language Query (NLQ) to SQL Translator

This project is an assignment for the subject of Database Management Systems (DBMS). The goal is to build a program that can translate natural language questions (in plain English) into executable SQL queries.

The project is built iteratively, with each version adding new functionality and complexity.

## Current Features

As of now, the translator can handle:

* **Basic Queries:** Simple, single-condition queries on a known table.
* **Multi-Condition Queries:** Queries containing two conditions linked by `AND` or `OR`.
* **Rule-Based Parsing:** The logic is built on a rule-based system using Regular Expressions in Python to identify and extract key query components.

## Project Structure & Solutions

The project is divided into different versions, each contained in its own folder. Each folder is a self-contained solution with its own README explaining its specific features and how to run it.

* **[V1: Basic Rule-Based](./V1_Basic_Rule_Based/)**: The foundational script that handles single conditions (e.g., "marks above 80").
* **[V2: Multi-Condition Queries](./V2_Multi_Condition/)**: An upgraded script that adds support for `AND` / `OR` clauses.

## Technology Used

* **Python 3**
* **Regular Expressions (Regex)**

## How to Use

1.  Clone this repository.
2.  Navigate into one of the version folders (e.g., `cd V2_Multi_Condition`).
3.  Follow the instructions in that folder's specific `README.md` file to run the script.
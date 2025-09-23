# Lab Solution: SQL Joins Investigation

Module X, activity Y — Applying INNER, LEFT, and RIGHT joins to correlate machines, employees, and login attempts.

In this solution I document each join operation used to answer investigative questions about device assignment and authentication events. I show raw queries, refined versions, and validation checks of row counts or NULL distribution.

---
### Task 1. Match employees to their machines
Goal: Identify which employees are using which machines by joining `machines` and `employees` on the shared `device_id`.

Initial exploration of both tables:
```sql
SELECT * FROM machines LIMIT 10;
```
```sql
+--------------+------------------+----------------+---------------+-------------+
| device_id    | operating_system | email_client   | OS_patch_date | employee_id |
+--------------+------------------+----------------+---------------+-------------+
| a184b775c707 | OS 1             | Email Client 1 | 2021-09-01    |        1156 |
| a192b174c940 | OS 2             | Email Client 1 | 2021-06-01    |        1052 |
| a305b818c708 | OS 3             | Email Client 2 | 2021-06-01    |        1182 |
| a317b635c465 | OS 1             | Email Client 2 | 2021-03-01    |        1130 |
| a320b137c219 | OS 2             | Email Client 2 | 2021-03-01    |        1000 |
| a398b471c573 | OS 3             | Email Client 2 | 2021-12-01    |           0 |
| a667b270c984 | OS 1             | Email Client 1 | 2021-03-01    |        1078 |
| a821b452c176 | OS 2             | Email Client 2 | 2021-12-01    |        1104 |
| a998b568c863 | OS 3             | Email Client 1 | 2021-12-01    |        1026 |
| b157c491d493 | OS 2             | Email Client 1 | 2021-03-01    |           0 |
+--------------+------------------+----------------+---------------+-------------+
(10 rows)
```

Perform inner join (replace placeholders X/Y in original instructions):
```sql
SELECT *
FROM machines
INNER JOIN employees ON machines.device_id = employees.device_id LIMIT 10;
```

```sql
+--------------+------------------+----------------+---------------+-------------+-------------+--------------+----------+------------------------+-------------+
| device_id    | operating_system | email_client   | OS_patch_date | employee_id | employee_id | device_id    | username | department             | office      |
+--------------+------------------+----------------+---------------+-------------+-------------+--------------+----------+------------------------+-------------+
| a320b137c219 | OS 2             | Email Client 2 | 2021-03-01    |        1000 |        1000 | a320b137c219 | elarson  | Marketing              | East-170    |
| b239c825d303 | OS 1             | Email Client 1 | 2021-03-01    |        1001 |        1001 | b239c825d303 | bmoreno  | Marketing              | Central-276 |
| c116d593e558 | OS 3             | Email Client 1 | 2021-09-01    |        1002 |        1002 | c116d593e558 | tshah    | Human Resources        | North-434   |
| d394e816f943 | OS 3             | Email Client 2 | 2021-03-01    |        1003 |        1003 | d394e816f943 | sgilmore | Finance                | South-153   |
| e218f877g788 | OS 2             | Email Client 1 | 2021-09-01    |        1004 |        1004 | e218f877g788 | eraab    | Human Resources        | South-127   |
| f551g340h864 | OS 3             | Email Client 2 | 2021-12-01    |        1005 |        1005 | f551g340h864 | gesparza | Human Resources        | South-366   |
| g329h357i597 | OS 1             | Email Client 2 | 2021-06-01    |        1006 |        1006 | g329h357i597 | alevitsk | Information Technology | East-320    |
| h174i497j413 | OS 2             | Email Client 1 | 2021-03-01    |        1007 |        1007 | h174i497j413 | wjaffrey | Finance                | North-406   |
| i858j583k571 | OS 2             | Email Client 2 | 2021-06-01    |        1008 |        1008 | i858j583k571 | abernard | Finance                | South-170   |
| k242l212m542 | OS 1             | Email Client 1 | 2021-03-01    |        1010 |        1010 | k242l212m542 | jlansky  | Finance                | South-109   |
+--------------+------------------+----------------+---------------+-------------+-------------+--------------+----------+------------------------+-------------+
10 rows in set (0.001 sec)
```


Validation checklist:
- All returned rows have a non‑NULL `device_id` in both tables.
- Row count equals the number of machines that are actually assigned.

> [!NOTE] Question
> How many rows did the inner join return?
> - [x] 185
> - [ ] 85
> - [ ] 124
> - [ ] 132

(Select the correct option based on lab output.)

---
### Task 2. Return more data with LEFT and RIGHT joins
Objective: Show all machines (even unassigned) then all employees (even without a machine).

LEFT join (keyword X from original prompt = LEFT):
```sql
SELECT *
FROM machines
LEFT JOIN employees ON machines.device_id = employees.device_id;
```
```sql
...
| f117g394h201 | OS 1             | Email Client 2 | 2021-03-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| g770h829i938 | OS 2             | Email Client 1 | 2021-09-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| s918t412u294 | OS 3             | Email Client 2 | 2021-12-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| t801u630v138 | OS 2             | Email Client 2 | 2021-03-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| u113v483w811 | OS 3             | Email Client 2 | 2021-06-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| v846w200x439 | OS 1             | Email Client 1 | 2021-06-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| w981x771y326 | OS 2             | Email Client 2 | 2021-06-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| x561y839z458 | OS 2             | Email Client 1 | 2021-09-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| y246z508a775 | OS 2             | Email Client 1 | 2021-12-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
| z821a946b264 | OS 3             | Email Client 2 | 2021-06-01    |           0 |        NULL | NULL         | NULL     | NULL                   | NULL        |
+--------------+------------------+----------------+---------------+-------------+-------------+--------------+----------+------------------------+-------------+
200 rows in set (0.007 sec)
```

Validation focus:
- Unassigned machines appear with `NULL` employee columns.
- Count of rows equals total rows in `machines`.

> [!NOTE] Question
> What is the value in the username column for the last record returned (LEFT JOIN)?
> - [x] NULL
> - [ ] areyes
> - [ ] cgriffin
> - [ ] asundara

RIGHT join (keyword X from original prompt = RIGHT):
```sql
SELECT *
FROM machines
RIGHT JOIN employees ON machines.device_id = employees.device_id;
```
```sql
...
| NULL         | NULL             | NULL           | NULL          |        NULL |        1190 | NULL         | kcarter  | Marketing              | Central-270 |
| NULL         | NULL             | NULL           | NULL          |        NULL |        1191 | NULL         | shakimi  | Marketing              | Central-366 |
| k570l183m949 | OS 3             | Email Client 1 | 2021-12-01    |        1192 |        1192 | k570l183m949 | rlaghari | Information Technology | East-138    |
| l186m618n319 | OS 1             | Email Client 2 | 2021-12-01    |        1193 |        1193 | l186m618n319 | esantiag | Information Technology | Central-300 |
| m340n287o441 | OS 2             | Email Client 2 | 2021-09-01    |        1194 |        1194 | m340n287o441 | zwarren  | Human Resources        | West-212    |
| n516o853p957 | OS 1             | Email Client 1 | 2021-09-01    |        1195 |        1195 | n516o853p957 | orainier | Finance                | East-346    |
| o225p357q829 | OS 3             | Email Client 1 | 2021-12-01    |        1196 |        1196 | o225p357q829 | sshah2   | Information Technology | South-385   |
| p791q114r509 | OS 2             | Email Client 1 | 2021-09-01    |        1197 |        1197 | p791q114r509 | aabara   | Information Technology | North-159   |
| q308r573s459 | OS 3             | Email Client 1 | 2021-03-01    |        1198 |        1198 | q308r573s459 | jmartine | Marketing              | South-117   |
| r520s571t459 | OS 2             | Email Client 2 | 2021-03-01    |        1199 |        1199 | r520s571t459 | areyes   | Human Resources        | East-100    |
+--------------+------------------+----------------+---------------+-------------+-------------+--------------+----------+------------------------+-------------+
200 rows in set (0.001 sec)
```

Validation focus:
- Employees without machines have `NULL` machine fields.
- Row count equals total rows in `employees`.

> [!NOTE] Question
> What is the value in the username column for the last record returned (RIGHT JOIN)?
> - [x] areyes
> - [ ] cgriffin
> - [ ] asundara
> - [ ] NULL

---
### Task 3. Retrieve login attempt data
Goal: List all login attempts along with employee attributes by joining `employees` and `log_in_attempts` on `username`.

Query template with placeholders from activity replaced:
```sql
SELECT *
FROM employees
INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;
```
```sql
  0 |
|        1035 | j236k303l245 | bisles   | Sales                  | South-171   |      192 | bisles   | 2022-05-10 | 08:32:03   | USA     | 192.168.201.40  |       0 |
|        1009 | NULL         | lrodriqu | Sales                  | South-134   |      193 | lrodriqu | 2022-05-08 | 07:11:29   | US      | 192.168.125.240 |       0 |
|        1017 | r550s824t230 | jclark   | Finance                | North-188   |      194 | jclark   | 2022-05-12 | 14:11:04   | CAN     | 192.168.197.247 |       0 |
|        1006 | g329h357i597 | alevitsk | Information Technology | East-320    |      195 | alevitsk | 2022-05-11 | 06:59:13   | CANADA  | 192.168.236.78  |       0 |
|        1042 | q175r338s833 | acook    | Human Resources        | West-381    |      196 | acook    | 2022-05-10 | 09:56:48   | CAN     | 192.168.52.90   |       0 |
|        1015 | p611q262r945 | jsoto    | Finance                | North-271   |      197 | jsoto    | 2022-05-08 | 09:05:09   | US      | 192.168.36.21   |       0 |
|        1033 | NULL         | yappiah  | Information Technology | West-387    |      198 | yappiah  | 2022-05-12 | 10:37:22   | MEXICO  | 192.168.103.106 |       0 |
|        1033 | NULL         | yappiah  | Information Technology | West-387    |      199 | yappiah  | 2022-05-11 | 19:34:48   | MEXICO  | 192.168.44.232  |       0 |
|        1017 | r550s824t230 | jclark   | Finance                | North-188   |      200 | jclark   | 2022-05-12 | 01:11:45   | CANADA  | 192.168.91.103  |       0 |
+-------------+--------------+----------+------------------------+-------------+----------+----------+------------+------------+---------+-----------------+---------+
200 rows in set (0.008 sec)
```

Row count should equal number of login attempt records that have a matching employee.

> [!NOTE] Question
> How many records are returned by this inner join?
> - [x] 200
> - [ ] 175
> - [ ] 210
> - [ ] 145

---
### Validation
- Inner join only returns rows where a machine and employee share a `device_id`.
- LEFT join preserves every machine; RIGHT join preserves every employee.
- Final inner join on login attempts confirms authentication events align to existing users (no orphan usernames).

### Notes
- Consider projecting only needed columns (e.g., `machines.device_id, employees.username`) for performance.
- Add `COUNT(*)` aggregation variants to store metrics in documentation.
- For NULL diagnostics, use predicates like `WHERE employees.username IS NULL` after a LEFT join variant to list unassigned devices.


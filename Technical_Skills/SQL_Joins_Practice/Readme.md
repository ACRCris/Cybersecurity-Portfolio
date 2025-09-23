# Activity Summary 
Module 4, Lab 5 from Tools of the Trade: Linux and SQL (Google Cybersecurity Certificate): Practice focused on using SQL joins to correlate device assignments and login attempts.

![alt text](ActivityResult.png)

In this activity, I used INNER, LEFT, and RIGHT joins to combine `machines`, `employees`, and `log_in_attempts` tables. I identified which devices were assigned, which employees lacked a device, unassigned machines, and consolidated authentication attempts with associated user attributes.

## Objectives accomplished
- Matched employees to machines via INNER JOIN on `device_id`.
- Listed all machines with possible NULL employees using LEFT JOIN.
- Listed all employees (including those without machines) using RIGHT JOIN.
- Correlated login attempts to employees via INNER JOIN on `username`.
- Distinguished assigned vs unassigned assets using NULL checks.
- Validated row counts for each join type to ensure correctness.

## Folder Structure and Status
- `LabSolution.md`: Step-by-step joins with queries, questions, and validation.
- `activity_sql_join.md`: Source activity instructions (original content moved here for reference).

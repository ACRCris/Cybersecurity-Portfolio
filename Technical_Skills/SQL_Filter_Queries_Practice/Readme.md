# Activity Summary 
Module 3, activity 1 from Tools of the Trade: Linux and SQL (Google Cybersecurity Certificate): Practice focused on applying logical SQL filters to authentication and employee data.

In this activity, I wrote SQL queries that filtered login attempts and employee records to investigate security-relevant patterns: failed logins after hours, activity on specific dates, access originating outside a defined country, departmental scope (Marketing in East offices), membership in target business units (Finance or Sales), and exclusion of a sensitive department (Information Technology). I reinforced translating investigative requirements into clear WHERE clauses using logical operators, pattern matching, set membership, and negation.

## Objectives accomplished

- Retrieved failed login attempts after business hours (post 18:00) using time and success status filters.
- Retrieved login attempts on two specific dates with an `IN` predicate for clarity.
- Retrieved login attempts originating outside Mexico by negating a prefix pattern (`NOT LIKE 'MEX%'`).
- Retrieved Marketing employees located in East building offices via combined `LIKE` filters.
- Retrieved employees in Finance or Sales using set membership (`IN`).
- Retrieved employees not in Information Technology with an inequality comparison.
- Consolidated results and rationale to confirm each investigative requirement was satisfied.

## Folder Structure and Status

- `ApplyFiltersToSqlQueries.md`: Main query development file.
- `InstructionsIncludingSqlQueries.md`: Instructions template for embedding executed queries.
- `TableFormats.md`: Reference describing table field formats.


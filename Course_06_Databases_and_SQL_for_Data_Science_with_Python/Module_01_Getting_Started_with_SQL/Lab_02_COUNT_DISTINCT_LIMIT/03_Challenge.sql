-- ============================================================
-- LAB 02 CHALLENGES: COUNT, DISTINCT, LIMIT
-- =========================================================
-- Challenge 1: COUNT
-- Count the number of film records directed by Woody Allen
SELECT
    COUNT(*)
FROM
    FilmLocations
WHERE
    Director = "Woody Allen";

-- Challenge 2: DISTINCT
-- Retrieve unique production companies for films released in 2015
SELECT
    DISTINCT ProductionCompany
FROM
    FilmLocations
WHERE
    ReleaseYear = 2015;

-- Challenge 3: LIMIT + OFFSET
-- Retrieve 5 film titles after skipping the first 10 films
SELECT
    Title
FROM
    FilmLocations
LIMIT
    5 OFFSET 10;
-- IBM Lab: COUNT examples
-- Query 1: Count all rows
SELECT
    COUNT(*)
FROM
    FilmLocations;

-- Query 2: Count locations for films written by James Cameron
SELECT
    COUNT(Locations)
FROM
    FilmLocations
WHERE
    Writer = "James Cameron";

-- Query 3: Retrieve unique film titles
SELECT
    DISTINCT Title
FROM
    FilmLocations;

-- Query 4: Count distinct release years for films produced by a specific company
SELECT
    COUNT(DISTINCT ReleaseYear)
FROM
    FilmLocations
WHERE
    ProductionCompany = "Warner Bros. Pictures";

-- Query 5: Retrieve the first 25 rows
SELECT
    *
FROM
    FilmLocations
LIMIT
    25;


-- Query 6: Retrieve 15 rows starting from row 11
SELECT
    *
FROM
    FilmLocations
LIMIT
    15 OFFSET 10;
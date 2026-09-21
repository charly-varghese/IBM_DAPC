-- ============================================
-- MY PRACTICE: Simple SELECT Queries
-- ============================================
-- Practice 1: View all records
SELECT
    *
FROM
    FilmLocations;

-- Practice 2: View selected columns
SELECT
    Title,
    ReleaseYear,
    Director
FROM
    FilmLocations;

-- Practice 3: Films released after 2010
SELECT
    Title,
    ReleaseYear,
    ProductionCompany
FROM
    FilmLocations
WHERE
    ReleaseYear > 2010;

-- Practice 4: Films released before 1990
SELECT
    Title,
    ReleaseYear,
    Locations
FROM
    FilmLocations
WHERE
    ReleaseYear < 1990;

-- Practice 5: Films not directed by Steven Spielberg
SELECT
    Title,
    Director,
    ReleaseYear
FROM
    FilmLocations
WHERE
    Director <> 'Steven Spielberg';
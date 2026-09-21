-- ============================================
-- CHALLENGE: Simple SELECT Queries
-- ============================================
-- Challenge 1:
-- Retrieve films released from 2020 onwards
SELECT
    Title,
    ReleaseYear,
    Director
FROM
    FilmLocations
WHERE
    ReleaseYear >= 2020;

-- Challenge 2:
-- Retrieve films produced by Netflix
SELECT
    Title,
    ProductionCompany,
    ReleaseYear
FROM
    FilmLocations
WHERE
    ProductionCompany = 'Netflix';

-- Challenge 3:
-- Retrieve films released after 2010
-- that were not directed by Steven Spielberg
SELECT
    Title,
    ReleaseYear,
    Locations
FROM
    FilmLocations
WHERE
    ReleaseYear > 2010
    AND Director <> 'Steven Spielberg';
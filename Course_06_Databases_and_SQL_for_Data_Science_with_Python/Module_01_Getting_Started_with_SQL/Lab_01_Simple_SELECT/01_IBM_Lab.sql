SELECT
    *
FROM
    FilmLocations;

SELECT
    Title,
    Director,
    Writer
FROM
    FilmLocations;

SELECT
    Title,
    ReleaseYear,
    Locations
FROM
    FilmLocations
WHERE
    ReleaseYear >= 2001;

SELECT
    FunFacts,
    Locations
FROM
    filmLocations;

    -- Query 5: Films released in 2000 and earlier

SELECT
    Title,
    Locations,
    ReleaseYear
FROM
    FilmLocations
WHERE
    ReleaseYear <= 2000;

    -- Query 6: Films not written by James Cameron

SELECT
    Title,
    ProductionCompany,
    Locations,
    ReleaseYear
FROM
    FilmLocations
WHERE
    Writer <> 'James Cameron';
    
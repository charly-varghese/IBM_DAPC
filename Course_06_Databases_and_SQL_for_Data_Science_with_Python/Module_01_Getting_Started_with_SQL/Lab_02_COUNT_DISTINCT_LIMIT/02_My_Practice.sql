-- Practice 1: Count the number of film locations directed by Woody Allen
SELECT
    COUNT(Locations)
FROM
    FilmLocations
WHERE
    Director = "Woody Allen";

-- Practice 2: Count the number of films shot at Russian Hill
SELECT
    COUNT(*)
FROM
    FilmLocations
WHERE
    Locations = "Russian Hill";

-- Practice 3: Count films released before 1950
SELECT
    COUNT(*)
FROM
    FilmLocations
WHERE
    ReleaseYear < 1950;

-- Practice 4: Retrieve unique films released in the 21st century
SELECT
    DISTINCT Title,
    ReleaseYear
FROM
    FilmLocations
WHERE
    ReleaseYear >= 2001;

-- Practice 5: Retrieve directors and distinct films shot at City Hall
SELECT
    DISTINCT Director,
    Title
FROM
    FilmLocations
WHERE
    Locations = "City Hall";

-- Practice 6: Count distinct distributors for films starring Clint Eastwood
SELECT
    COUNT(DISTINCT Distributor)
FROM
    FilmLocations
WHERE
    Actor1 = "Clint Eastwood";

-- Practice 7: Retrieve the names of the first 50 films
SELECT
    Title
FROM
    FilmLocations
LIMIT
    50;

-- Practice 8: Retrieve the first 10 film names released in 2015
SELECT
    Title
FROM
    FilmLocations
WHERE
    ReleaseYear = 2015
LIMIT
    10;

-- Practice 9: Retrieve the next 3 films after the first 5 films released in 2015
SELECT
    Title
FROM
    FilmLocations
WHERE
    ReleaseYear = 2015
LIMIT
    3 OFFSET 5;
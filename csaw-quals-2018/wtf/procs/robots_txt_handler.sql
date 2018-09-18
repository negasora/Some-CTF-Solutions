BEGIN
    SET status = 200;
    SET resp = CONCAT('User-agent: *
', (SELECT GROUP_CONCAT(CONCAT('Disallow: ', `match`, ' # procedure:', proc) SEPARATOR '
') FROM `routes`), '

# Yeah, we know this is contrived :(');
END
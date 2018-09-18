BEGIN
    IF EXISTS(SELECT 1 FROM `static_assets` WHERE `path` = route) THEN
        SET status = 200;
        SET resp = (SELECT `data` FROM `static_assets` WHERE `path` = route);
    ELSE
        SET status = 404;
        SET resp = 'Static file not found.';
    END IF;
END
BEGIN
    DECLARE template_s TEXT;

    IF EXISTS(SELECT 1 FROM `templates` WHERE `path` = template_name) THEN
        SET template_s = (SELECT `data` FROM `templates` WHERE `path` = template_name LIMIT 1);
    ELSE
        SET template_s = CONCAT('ERROR: NO TEMPLATE FOUND WITH NAME: ', template_name);
    END IF;

    CALL template_string(template_s, resp);
END
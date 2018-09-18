BEGIN
    IF EXISTS(SELECT 1 FROM `cookies` WHERE `name` = `i_name`) THEN
        SET `o_value` = (SELECT `value` FROM `cookies` WHERE `name` = `i_name` LIMIT 1);
    ELSE
        SET `o_value` = NULL;
    END IF;
END
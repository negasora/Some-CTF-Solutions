BEGIN
    IF EXISTS(SELECT 1 FROM `query_params` WHERE `name` = i_name) THEN
        SET o_value = (SELECT `value` FROM `query_params` WHERE `name` = i_name LIMIT 1);
    END IF;
END
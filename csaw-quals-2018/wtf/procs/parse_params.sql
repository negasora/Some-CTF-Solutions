BEGIN
    
    DECLARE cur_params, param, encoded_param_name, param_name, encoded_param_value, param_value TEXT;
    SET cur_params = params;

    WHILE ( INSTR(cur_params, '=') > 0 ) DO 
        SET param = SUBSTRING_INDEX(cur_params, '&', 1);

        SET encoded_param_name = TRIM(SUBSTRING(param FROM 1 FOR INSTR(param, '=') - 1));
        SET encoded_param_value = TRIM(SUBSTRING(param FROM INSTR(param, '=') + 1));

        SET encoded_param_name = REPLACE(encoded_param_name, '+', ' ');
        SET encoded_param_value = REPLACE(encoded_param_value, '+', ' ');

        CALL urldecode(encoded_param_name, param_name);
        CALL urldecode(encoded_param_value, param_value);

        INSERT INTO `query_params` VALUES (param_name, param_value) ON DUPLICATE KEY UPDATE `value` = param_value;

        SET cur_params = SUBSTRING(cur_params FROM LENGTH(param) + 2);
    END WHILE;
END
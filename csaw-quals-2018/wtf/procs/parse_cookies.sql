BEGIN
    
    DECLARE cookie_value BLOB;
    DECLARE cur_cookies, cookie, cookie_name, cookie_value_and_sig TEXT;
    DECLARE cookie_valid BOOLEAN;

    SET cur_cookies = cookies;

    WHILE ( INSTR(cur_cookies, '=') > 0 ) DO
        SET cookie = SUBSTRING_INDEX(cur_cookies, ';', 1);
        
        SET cookie_name = TRIM(SUBSTRING(cookie FROM 1 FOR INSTR(cookie, '=') - 1));
        SET cookie_value_and_sig = TRIM(SUBSTRING(cookie FROM INSTR(cookie, '=') + 1));

        CALL verify_cookie(cookie_value_and_sig, cookie_value, cookie_valid);

        IF cookie_valid THEN
            INSERT INTO `cookies` VALUES (cookie_name, cookie_value) ON DUPLICATE KEY UPDATE `value` = cookie_value;
        END IF;

        
        
        SET cur_cookies = TRIM(SUBSTRING(cur_cookies FROM LENGTH(cookie) + 2));
    END WHILE;
END
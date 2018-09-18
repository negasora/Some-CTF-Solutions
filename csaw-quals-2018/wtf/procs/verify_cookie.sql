BEGIN
    DECLARE secret, signature TEXT;
    SET secret = (SELECT `value` FROM `config` WHERE `name` = 'signing_key');
    
    SET signature = SUBSTR(signed_value FROM 1 FOR 64);
    SET cookie_value = UNHEX(SUBSTR(signed_value FROM 65));

    SET valid = (SELECT SHA2(CONCAT(cookie_value, secret), 256) = signature);
END
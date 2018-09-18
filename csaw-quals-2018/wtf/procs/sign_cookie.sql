BEGIN
    DECLARE secret, signature TEXT;
    SET secret = (SELECT `value` FROM `config` WHERE `name` = 'signing_key');

    SET signature = SHA2(CONCAT(cookie_value, secret), 256);

    SET signed = CONCAT(signature, LOWER(HEX(cookie_value)));
END
BEGIN
    DECLARE signed_value TEXT;
    CALL sign_cookie(i_value, signed_value);

    INSERT INTO `resp_cookies` VALUES (i_name, signed_value) ON DUPLICATE KEY UPDATE `value` = signed_value;
END
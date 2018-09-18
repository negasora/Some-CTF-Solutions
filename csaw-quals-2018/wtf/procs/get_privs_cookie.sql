BEGIN
    DECLARE privs, signing_key TEXT;

    SET privs = COALESCE((SELECT GROUP_CONCAT(priv SEPARATOR ';') FROM `admin_privs` WHERE `email` = i_email), '');

    SET signing_key = (SELECT `value` FROM `priv_config` WHERE `name` = 'signing_key');

    SET signed_privs = CONCAT(MD5(CONCAT(signing_key, privs)), privs);
END
BEGIN
    DECLARE privs, cur_privs, cmp_priv BLOB;
    DECLARE hash, signing_key TEXT;

    SET o_has_priv = FALSE;

    SET privs = NULL;
    CALL get_cookie('privs', privs);

    IF NOT ISNULL(privs) THEN
        SET hash = SUBSTR(privs FROM 1 FOR 32);
        SET cur_privs = SUBSTR(privs FROM 33);
        SET signing_key = (SELECT `value` FROM `priv_config` WHERE `name` = 'signing_key');

        IF hash = MD5(CONCAT(signing_key, cur_privs)) THEN
            WHILE ( LENGTH(cur_privs) > 0 ) DO
                SET cmp_priv = SUBSTRING_INDEX(cur_privs, ';', 1);
                IF cmp_priv = i_priv THEN
                    SET o_has_priv = TRUE;
                END IF;
                SET cur_privs = SUBSTR(cur_privs FROM LENGTH(cmp_priv) + 2);
            END WHILE;
        END IF;
    END IF;
END
BEGIN
    DECLARE `is_admin_cookie` TEXT;

    SET `is_admin_cookie` = NULL;
    CALL get_cookie('admin', `is_admin_cookie`);

    SET o_admin = (`is_admin_cookie` = TRUE);
END
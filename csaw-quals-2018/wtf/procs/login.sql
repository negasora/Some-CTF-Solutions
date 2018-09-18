BEGIN
    DECLARE is_admin BOOLEAN;
    DECLARE privs TEXT;

    SET is_admin = (SELECT `admin` FROM `users` WHERE `email` = `i_email`);
    CALL get_privs_cookie(i_email, privs);

    CALL set_cookie('admin', `is_admin`);
    CALL set_cookie('email', `i_email`);
    CALL set_cookie('privs', `privs`);
END
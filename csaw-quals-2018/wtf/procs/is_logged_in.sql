BEGIN
    DECLARE `u_email` TEXT;

    SET `u_email` = NULL;
    CALL get_cookie('email', `u_email`);

    IF ISNULL(`u_email`) THEN
        SET o_logged_in = FALSE;
    ELSE
        SET o_logged_in = EXISTS(SELECT 1 FROM `users` WHERE `email` = `u_email`);
    END IF;
END
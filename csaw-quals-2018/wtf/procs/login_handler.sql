BEGIN
    DECLARE email, password TEXT;
    DECLARE auth BOOLEAN;
    
    SET `email` = NULL;
    SET `password` = NULL;

    CALL get_param('email', `email`);
    CALL get_param('password', `password`);

    IF ISNULL(`email`) OR ISNULL(`password`) THEN
        SET status = 200;
        CALL template('/templates/login.html', resp);
    ELSE
        CALL check_password(`email`, `password`, `auth`);
        IF auth THEN
            SET resp = CONCAT(`email`, ', ', `password`);
            CALL login(`email`);
            CALL redirect('/', status);
        ELSE
            SET status = 401;
            
            CALL set_template_var('error_msg', 'Email or password is incorrect.');
            CALL template('/templates/404.html', resp);
        END IF;
    END IF;
END
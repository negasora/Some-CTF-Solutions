BEGIN
    DECLARE logged_in BOOLEAN;

    CALL is_logged_in(logged_in);
    if logged_in THEN
        CALL logged_in_index_handler(status, resp);
    ELSE
        SET resp = 'redirecting to register...';
        CALL redirect('/register', status);
    END IF;
END
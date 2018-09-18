BEGIN
    DECLARE logged_in BOOLEAN;
    DECLARE u_email TEXT;
    DECLARE user_id INT;
    DECLARE post_text TEXT;

    SET resp = '';

    CALL is_logged_in(logged_in);
    IF logged_in THEN
        CALL get_cookie('email', u_email);
        CALL get_param('post', post_text);
        SET user_id = (SELECT `id` FROM `users` WHERE `email` = u_email);

        IF EXISTS (SELECT 1 FROM `banned_post_patterns` WHERE `post_text` REGEXP `pattern`) THEN
            SET status = 200;
            SET resp = 'Banned word used in post!';
        ELSE
            CALL create_post(user_id, post_text);
            CALL redirect('/', status);
        END IF;

    ELSE
        CALL redirect('/login', status);
    END IF;
END
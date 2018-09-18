BEGIN
    SET o_exists = EXISTS(SELECT 1 FROM `users` WHERE `email` = i_email);
END
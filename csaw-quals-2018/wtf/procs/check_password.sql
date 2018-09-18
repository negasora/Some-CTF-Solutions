BEGIN
    DECLARE hashed TEXT;
    SET hashed = (SELECT SHA2(password, 256));
    SET correct = EXISTS(SELECT 1 FROM `users` WHERE `email` = email AND `pass_hash` = hashed);
END
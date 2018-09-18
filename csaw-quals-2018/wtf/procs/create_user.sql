BEGIN
    DECLARE hashed TEXT;
    SET hashed = (SELECT SHA2(password, 256));
    INSERT INTO `users` (`email`, `name`, `pass_hash`) VALUES (email, name, hashed);
END
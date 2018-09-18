BEGIN
    DECLARE encoded_post TEXT;
    CALL htmlentities(i_text, encoded_post);

    INSERT INTO `posts` (`user_id`, `text`) VALUES (`i_user_id`, `encoded_post`);
END
BEGIN
    DECLARE done BOOLEAN;
    DECLARE curr_row TEXT;
    DECLARE posts_cur CURSOR FOR SELECT CONCAT('<li><div class=post-text>', `text`, '</div></li>') FROM `posts` WHERE `user_id` = `i_user_id` LIMIT 50;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    SET o_post_list = '';
    OPEN posts_cur;
    posts_loop: LOOP
        FETCH posts_cur INTO curr_row;
        IF done THEN
            CLOSE posts_cur;
            LEAVE posts_loop;
        END IF;

        SET o_post_list = CONCAT(o_post_list, curr_row);
    END LOOP posts_loop;
END
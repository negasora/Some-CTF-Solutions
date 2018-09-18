BEGIN
    SET o_status = 302;
    CALL set_header('Location', i_location);
END
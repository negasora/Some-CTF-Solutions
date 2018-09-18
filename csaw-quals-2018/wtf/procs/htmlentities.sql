BEGIN
    SET o_str = REPLACE(REPLACE(i_str, '<', '&lt;'), '>', '&gt;');
END
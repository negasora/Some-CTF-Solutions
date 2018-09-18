BEGIN
    DECLARE db_name, tbl_name, cols TEXT;

    IF INSTR(i_table_name, '.') THEN
        SET db_name = SUBSTRING_INDEX(i_table_name, '.', 1);
        SET tbl_name = SUBSTR(i_table_name FROM INSTR(i_table_name, '.') + 1);
    ELSE
        SET db_name = DATABASE();
        SET tbl_name = i_table_name;
    END IF;

    SET cols = NULL;
    SET cols = (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE `table_schema` = `db_name` AND `table_name` = `tbl_name`);

    IF ISNULL(cols) THEN
        SET o_html = 'No such table';
    ELSE
        SET @dump_query = (SELECT CONCAT('SELECT CONCAT('<tr>', GROUP_CONCAT(CONCAT('<td>', CONCAT_WS('</td><td>', ', cols, '), '</td>') SEPARATOR '</tr><tr>'), '</tr>') INTO @dump_result FROM ', `i_table_name`, ';'));
        PREPARE prepped_query FROM @dump_query;
        EXECUTE prepped_query;

        SET cols = (SELECT CONCAT('<tr><td>', GROUP_CONCAT(column_name SEPARATOR '</td><td>'), '</td></tr>') FROM information_schema.columns WHERE `table_schema` = `db_name` AND `table_name` = `tbl_name`);
        SET o_html = CONCAT('<table>', cols, @dump_result, '</table>');
    END IF;
END
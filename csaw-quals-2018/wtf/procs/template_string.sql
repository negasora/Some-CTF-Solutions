BEGIN
    DECLARE formatted TEXT;
    DECLARE fmt_name, fmt_val TEXT;
    DECLARE replace_start, replace_end, i INT;

    SET @template_regex = '\$\{[a-zA-Z0-9_ ]+\}';

    CREATE TEMPORARY TABLE IF NOT EXISTS `template_vars` (`name` VARCHAR(255) PRIMARY KEY, `value` TEXT);
    CALL populate_common_template_vars();

    SET formatted = template_s;
    SET i = 0;

    WHILE ( formatted REGEXP @template_regex AND i < 50 ) DO
        SET replace_start = REGEXP_INSTR(formatted, @template_regex, 1, 1, 0);
        SET replace_end = REGEXP_INSTR(formatted, @template_regex, 1, 1, 1);
        SET fmt_name = SUBSTR(formatted FROM replace_start + 2 FOR (replace_end - replace_start - 2 - 1));
        SET fmt_val = (SELECT `value` FROM `template_vars` WHERE `name` = TRIM(fmt_name));
        SET fmt_val = COALESCE(fmt_val, '');
        SET formatted = CONCAT(SUBSTR(formatted FROM 1 FOR replace_start - 1), fmt_val, SUBSTR(formatted FROM replace_end));
        SET i = i + 1;
    END WHILE;

    SET resp = formatted;

    DROP TEMPORARY TABLE `template_vars`;
END
BEGIN
    DECLARE decoded TEXT;
    DECLARE hex CHAR(2);

    SET decoded = i_str;

    WHILE (INSTR(decoded, '%') > 0) DO
        SET hex = SUBSTR(decoded FROM INSTR(decoded, '%') + 1 FOR 2);
        SET decoded = CONCAT(SUBSTR(decoded FROM 1 FOR INSTR(decoded, '%') - 1), UNHEX(hex), SUBSTR(decoded FROM INSTR(decoded, '%') + 3));
    END WHILE;

    SET o_str = decoded;
END
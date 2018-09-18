BEGIN
    CREATE TEMPORARY TABLE IF NOT EXISTS `template_vars` (`name` VARCHAR(255) PRIMARY KEY, `value` TEXT);
    INSERT INTO `template_vars` VALUES (`i_key`, `i_value`);
END
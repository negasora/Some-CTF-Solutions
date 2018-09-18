BEGIN
    INSERT INTO `resp_headers` VALUES (`name`, `value`) ON DUPLICATE KEY UPDATE `value` = `value`;
END
BEGIN
    INSERT INTO `template_vars` SELECT CONCAT('config_', name), value FROM `config`;
    INSERT INTO `template_vars` SELECT CONCAT('request_', name), value FROM `query_params`;
END
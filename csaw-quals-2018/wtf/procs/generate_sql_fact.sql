BEGIN
    INSERT INTO `resp_headers` VALUES ('X-SQL-Fact', (SELECT `fact` FROM `sql_facts` ORDER BY RAND() LIMIT 1));
END
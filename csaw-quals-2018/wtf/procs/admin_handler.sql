BEGIN
    DECLARE u_email, table_name, rendered_table, html TEXT;
    DECLARE admin, can_view_panels, can_create_panels  BOOL;

    DECLARE done BOOLEAN;
    DECLARE panel_cur CURSOR FOR SELECT `tbl` FROM `panels` WHERE `email` = `u_email`;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    CALL is_admin(admin);

    IF admin THEN
        CALL get_cookie('email', u_email);

        CALL has_priv('panel_create', can_create_panels);
        CALL has_priv('panel_view', can_view_panels);

        SET html = CONCAT(can_view_panels, can_create_panels);
        SET rendered_table = '';

        IF can_create_panels THEN
            CALL get_param('tbl', table_name);

            IF table_name <> '' THEN
                INSERT INTO `panels` VALUES (`u_email`, `table_name`);
            END IF;

            CALL template('/templates/admin_create_panel_partial.html', rendered_table);
            SET html = CONCAT(html, rendered_table);
        END IF;

        SET rendered_table = '';
        IF can_view_panels THEN
            OPEN panel_cur;
            panels_loop: LOOP
                FETCH panel_cur INTO table_name;
                IF done THEN
                    CLOSE panel_cur;
                    LEAVE panels_loop;
                END IF;

                CALL dump_table_html(table_name, rendered_table);

                SET html = CONCAT(html, table_name, rendered_table, '<br/>');
            END LOOP panels_loop;
        END IF;

        DROP TEMPORARY TABLE IF EXISTS `template_vars`;
        CREATE TEMPORARY TABLE IF NOT EXISTS `template_vars` (`name` VARCHAR(255) PRIMARY KEY, `value` TEXT);
        INSERT INTO `template_vars` VALUES ('tables', html);

        SET status = 200;
        CALL template('/templates/admin.html', resp);
    ELSE
        SET status = 403;
        SET resp = 'You must be an admin to view this page.';
    END IF;
END
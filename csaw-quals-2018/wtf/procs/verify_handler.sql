BEGIN
    DECLARE proc TEXT;

    SET proc = NULL;
    CALL get_param('proc', proc);

    SET status = 200;
    IF ISNULL(proc) THEN
        SET resp = 'Missing required param 'proc'!';
    ELSE
        SET resp = COALESCE((SELECT routine_definition FROM information_schema.routines WHERE routine_name = proc), 'No such procedure!');
    END IF;
END
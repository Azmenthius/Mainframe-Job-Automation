/* check_job.rex - Check job status */
parse arg jobid
if jobid = '' then do
    say 'No job ID provided. Checking the most recent job...'
    
    logfile = 'output/logs.txt'
    if stream(logfile, 'C', 'QUERY EXISTS') = '' then do
        say 'No logs found!'
        exit 1
    end

    last_line = ''
    do while lines(logfile) > 0
        last_line = linein(logfile)
    end
    
    if last_line = '' then do
        say 'No job logs available!'
        exit 1
    end

    jobid = word(last_line, 3)  /* Extract Job ID */
    say 'Using latest job ID: ' jobid
end

/* Search logs for job ID */
logfile = 'output/logs.txt'
found = 0
do while lines(logfile) > 0
    log_entry = linein(logfile)
    if word(log_entry, 3) = jobid then do
        say log_entry
        found = 1
    end
end

if found = 0 then
    say 'No log entry found for job ID:' jobid

call lineout logfile  /* Close file */
exit 0

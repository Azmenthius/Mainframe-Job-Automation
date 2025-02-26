/* REXX script to retrieve job logs from SDSF */
/* Reads job logs from logs.txt */
/* retrieve_logs.rex - Retrieves all logs */
logfile = 'output/logs.txt'

if stream(logfile, 'C', 'QUERY EXISTS') = '' then do
    say 'No logs found!'
    exit 1
end

/* Read and display logs */
do while lines(logfile) > 0
    log_entry = linein(logfile)
    say log_entry
end

call lineout logfile  /* Close file */
exit 0


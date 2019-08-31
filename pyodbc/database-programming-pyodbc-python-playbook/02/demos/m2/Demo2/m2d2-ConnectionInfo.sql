USE [master];

SELECT sess.session_id,login_time,[host_name],[program_name],client_interface_name,login_name,dbs.[name] dbname,
[status],open_transaction_count, conns.net_packet_size
FROM 
sys.dm_exec_sessions sess 
INNER JOIN sys.databases dbs ON sess.database_id=dbs.database_id
INNER JOIN sys.dm_exec_connections conns ON sess.session_id=conns.session_id
WHERE [program_name] LIKE 'Pluralsight%';
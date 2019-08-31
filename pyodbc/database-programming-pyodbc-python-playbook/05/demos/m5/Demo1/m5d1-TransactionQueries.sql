SELECT sess_trans.session_id,open_transaction_count, sqltext.text 
FROM sys.dm_tran_session_transactions sess_trans 
INNER JOIN sys.dm_exec_connections conns ON conns.session_id = sess_trans.session_id
CROSS APPLY sys.dm_exec_sql_text(conns.most_recent_sql_handle) sqltext 

SELECT lcks.request_session_id,lcks.resource_type, request_mode, count(*) lockCount
FROM sys.dm_tran_locks lcks
INNER JOIN sys.dm_tran_session_transactions sess_trans ON sess_trans.session_id = lcks.request_session_id
INNER JOIN sys.dm_exec_connections conns ON conns.session_id = sess_trans.session_id
CROSS APPLY sys.dm_exec_sql_text(conns.most_recent_sql_handle) sqltext 
GROUP BY request_session_id,resource_type,request_mode

SELECT * 
FROM WideWorldImporters.sys.tables WITH(NOWAIT)
WHERE name = 'SpecialDeals-Copy1'

SELECT * FROM WideWorldImporters.[Sales].[SpecialDeals-Copy1]
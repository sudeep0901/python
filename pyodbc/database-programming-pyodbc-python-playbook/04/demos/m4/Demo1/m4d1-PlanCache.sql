SELECT
execution_count
,  [Database] = DB_NAME(qt.dbid)
,[Parent  Query] = qt.text
, qp.query_plan
FROM  sys.dm_exec_query_stats er
CROSS APPLY  sys.dm_exec_sql_text(er.sql_handle)as qt
CROSS APPLY sys.dm_exec_query_plan(er.plan_handle)as qp
WHERE qt.text LIKE '%--bool to bit%'


SELECT
execution_count
,  [Database] = DB_NAME(qt.dbid)
,[Parent  Query] = qt.text
, qp.query_plan
FROM  sys.dm_exec_query_stats er
CROSS APPLY  sys.dm_exec_sql_text(er.sql_handle)as qt
CROSS APPLY sys.dm_exec_query_plan(er.plan_handle)as qp
WHERE qt.text LIKE '%--unicode to varchar%'

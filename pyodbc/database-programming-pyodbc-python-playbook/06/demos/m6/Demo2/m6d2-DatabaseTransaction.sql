-- run this first to block 
BEGIN TRANSACTION
UPDATE WideWorldImporters.Sales.InvoiceLines
SET TaxRate = TaxRate + (TaxRate*0.05)

-- rollback to release locks
ROLLBACK


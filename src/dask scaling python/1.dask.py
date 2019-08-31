import dask.bag as db
from dask.distributed import Client

client = Client()
client
from dask.diagnostics import ProgressBar
import time
a_list = [1, 4, 10, 20]

simple_bag = db.from_sequence(a_list, npartitions=1)
out_put = simple_bag.map(lambda x: x + 1).compute()
print(out_put)
out_fold = simple_bag.fold(lambda acc, e: acc + e, initial=0).compute()
print(out_fold)

with ProgressBar():
    foldby_out = simple_bag.foldby(lambda x: x % 2 == 0,
lambda x, y: x + y, 
initial=0).compute()
print(foldby_out)
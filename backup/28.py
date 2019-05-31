def returnName(fname, lname):
    return fname + lname


import multiprocessing

pool = multiprocessing.Pool


async_result  = pool.apply_async(returnName, ("sudeep", "patel   "))

return_val = async_result.get()
def func_arg(*sudeep):
    for ar in sudeep:
        print(ar)

    
func_arg("Hellow", "how", 1)

def func_kwargs(par4="par4", **kwargs ):
    for k, v in kwargs.items():
        print(k, v)


func_kwargs(par="par1",par2="par1",par3="par1",)
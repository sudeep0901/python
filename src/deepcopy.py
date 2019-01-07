#Deep copy

import copy
adl = [1, 2, 3, [4, 5]]
bdl= copy.deepcopy(adl)

bdl[3][0] =-100
print(adl, bdl)
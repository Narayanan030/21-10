#array creation


#array
import numpy as np  
arr=np.array([1,2.,3.],ndmin=2)  
arr  

#arange
import numpy as np
np.arange(3)
np.arange(3.0)
np.arange(3,7)
np.arange(3,7,2)

#zeros
a = np.zeros((2, 3, 4))
a

#ones
import numpy as np
np.ones(5)

#linescape
import numpy as np
np.linspace(2.0, 3.0, num=5)
np.linspace(2.0, 3.0, num=5, endpoint=False)
np.linspace(2.0, 3.0, num=5, retstep=True)

#eye
import numpy as np
np.eye(2, dtype=int)
np.eye(3, k=1)

#empty
import numpy as np
np.empty([2, 2])

#full
import numpy as np
np.full((2, 2), np.inf)
np.full((2, 2), 10)

#random.rand
np.random.rand(3,2)

#random.randn
np.random.randn()
#array manipulation

#reshape
import numpy as np
a = np.arange(6).reshape((3, 2))
a

#flatten
import numpy as np
a = np.array([[1,2], [3,4]])
a.flatten()
a.flatten('F')

#ravel
 import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(np.ravel(x))

#transpose
import numpy as np
a = np.array([[1, 2], [3, 4]])
np.transpose(a)

#concatenate
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)

#stack
import numpy as np
rng = np.random.default_rng()
arrays = [rng.normal(size=(3,4)) for _ in range(10)]
np.stack(arrays, axis=0).shape

#vstack
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack((a,b))

#hstack
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
np.hstack((a,b))

#split
import numpy as np
x = np.arange(9.0)
np.split(x, 3)

#append
import numpy as np
np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
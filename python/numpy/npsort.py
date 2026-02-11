import numpy as np

dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals = [('Hrithik', 2009, 8.5),
        ('Ajay', 2008, 8.7),
        ('Pankaj', 2008, 7.9),
        ('Akash', 2009, 9.0),]

a = np.array(vals, dtype=dtype)
print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))
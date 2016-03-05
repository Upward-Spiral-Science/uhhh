import numpy
import csv

class SETUP():
    def __init__(self):
        data = open('../data/data.csv', 'r').readlines()
        fieldnames = ['x', 'y', 'z', 'unmasked', 'synapses']
        reader = csv.reader(data)
        reader.next()

        rows = [[int(col) for col in row] for row in reader]

        sorted_x = sorted(list(set([r[0] for r in rows])))
        sorted_y = sorted(list(set([r[1] for r in rows])))
        sorted_z = sorted(list(set([r[2] for r in rows])))

        # Pass-to-ranks volume, useful for reducing size of data.
        self.ptr_volume = numpy.ndarray((len(sorted_x), len(sorted_y), len(sorted_z)))
        # Real-life volume (persisting 3D space)
        self.volume = numpy.ndarray((max(sorted_x)+1, max(sorted_y)+1, max(sorted_z)+1))

        for row in rows:
            if row[-1] != 0:
                self.volume[row[0], row[1], row[2]] = row[-1]
                self.ptr_volume[sorted_x.index(row[0]), sorted_y.index(row[1]), sorted_z.index(row[2])] = row[-1]

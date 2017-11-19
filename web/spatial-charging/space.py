class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

class Space:
    def __init__(self, dim_lens=[0,0,0], partitions):
        self.dim_lens = dim_lens
        self.partitions = partitions

    def __init__(self, dim_lens=[0,0,0]):
        self.dim_lens = dim_lens

    get_dim_len(self, dim):
        return self.dim_lens[dim]

    make_partitions(self, size):
        partitions = []
        for x in range(0, get_dim_len(0)/size):
            for y in range(0, get_dim_len(1)/size):
                for z in range(0, get_dim_len(2)/size):
                    pos = map((lambda dim: dim * size), [x,y,z])
                    partitions.append(Partition(Space([size] * 3), pos))
        return partitions

class Partition():
    def __init__(self, space, pos=[0,0,0]):
        self.space = Space;
        self.pos =  

    def contains(coords):
        if 

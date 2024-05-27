# my_functions.py

def max_ring_size(mol):
    """Get the size of the largest ring in the molecule
    
    :param mol: input molecule
    
    :return: largest ring size or 0 for an acyclic molecule
    """

    ring = mol.GetRingInfo()
    atom_ring = ring.AtomRings()
    if len(atom_ring) == 0:
        return 0
    else:
       return max([len(x) for x in atom_ring])
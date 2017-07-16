from random import randint
from collections import namedtuple



def sample_generator(side_length):
    
    """Create a sample with grots"""
    
    sample = [[randint(1,4) for j in range(side_length)] for i in range(side_length)]
    
    vectors = {
        'u': (1,0),
        'd': (-1,0),
        'r': (0,1 ),
        'l': (0,-1),
    }

    letters = {
        1: 'u',
        2: 'd',
        3: 'r',
        4: 'l',
    }

    grots = {
        'u': "↑",
        'd': "↓",
        'r': "→",
        'l': "←",
    }
       
        
    # Now we converting the sample
    # to the values u,d,r,l

    
    for i in sample:
        for value, key in enumerate(i):
            i[value] = dictionar[key]

    # For better understanding how we perform
    # we visualise sample2 in more human-like view
    # with grots.
    
    sample2 = []
    
    for i in sample:
        row = []
        for j in i:
            row.append(j)
        sample2.append(row)
        
    for i in sample2:
        for value, key in enumerate(i):
            i[value] = grots[key]

    # Now we converting the sample to the vectors:
    # 1 - (1,0) - up.
    # 2 - (-1,0) - down,
    # 3 - (0,-1) - left,
    # 4 - (0,1) - right.

    
    for i in sample:
        for value, key in enumerate(i):
            i[value] = vectors[key]    

    return sample, sample2
    
    

class GrotSearcher():
    
    def __init__(self, sample, chains, o):
        self.sample = sample
        self.chains = chains
        self.o = o
        
    def if_point_has_history(self, chain, a, b):      

        """ If our point has a history (i.e. it """
        """ has beem verified) we will add it and """
        """ maybe its chain to chain being created """

        # Choose the chain with b,a from chains. 
        # If it contains sth - we will took only the first one
        # Else: we will take only the b,a. 
                
        chain_a_b = [i for i in self.chains if i[0] == (b,a)]
        
        if chain_a_b:
            chain_a_b = chain_a_b[0]
        else:    
            chain_a_b = [(b,a)]
        
        # Check if the b,a is not a pre-last
        # element of the chain
             
        temp_chain = chain + chain_a_b
       
        
        self.chains.append(temp_chain)               

    def backend(self):
        
        """It is our basic for searching the longest chain"""
        
        # for loops will give us coordinates that we will check
        
        for i in self.o:
            for j in self.o:
                x, y = j, i
                chain = []
                stop = 0               
                while True:
                    x, y, stop, chain = self.step_by_step(x, y, stop, chain)
                    if stop == 1:
                        break
        
                
        return self.chains
        
    def step_by_step(self, x, y, stop, chain):
        
        """ input a coordinate we start at """ 
        """ output: new coordinates """
        """ + value of stop """
        """ + chain with starting coordinates"""
        
        wektor = self.sample[y][x]
        
        # if we  meet (2,2) [see below why]
        # we stop while loop in the self.backend
        
        if wektor == (2,2):
            chain.append((y, x))
            self.chains.append(chain)
            stop = 1
            return x, y, stop, chain        
        
        # We set (2,2) in order to indicate 
        # items we checked 
        # + add it to the chain being created 
        
        chain.append((y, x))
        self.sample[y][x] = (2, 2)
        
               
        if wektor[0] == 1: # up
            a, b = x, y - 1 
        elif wektor[0] == -1: # down
            a, b = x, y + 1

        elif wektor[1] == -1: #left
            a, b = x - 1, y
        else:                 #right
            a, b = x + 1, y    
            
        if 0 <= a <= (len(self.o)-1) and (0 <= b <= len(self.o)-1): #if b,a are in the scope
            if self.sample[b][a] != (2, 2): #if it is not 2,2
                x, y = a, b
                return x, y, stop, chain
            else:                           #if it has a story, stop = 1
                self.if_point_has_history(chain, a, b)
                stop = 1
                return x, y, stop, chain
        else:
            self.chains.append(chain) #if b,a is out of the sample's boundaries
            stop = 1
            return x, y, stop, chain                    

class Viewer():
    
    @staticmethod
    def max_lens(chains):
        
        for num, i in enumerate(chains):
            try:
                if i[-1] == i[-3]:
                    chains[num] = i[:-1]
            except: 
                pass
                
        
        lens = [len(i) for i in chains]
        max_lens = []
        for num, i in enumerate(lens):
            if i == max(lens):
                max_lens.append(num)
        
        return max_lens
    
    @staticmethod
    def shower(max_lens, chains, sample2):
        
        print("Here our starting points:", sep= " ")
        for i in max_lens:
            position = namedtuple("row", "column")
            position.row = chains[i][0][0] + 1
            position.column = chains[i][0][1] + 1
            print("Row (from above): ", position.row, 
              "Column: ", position.column, 
              "Length: ", len(chains[i]), end="\n",)
            print(chains[i])
        for i in sample2:
            print(i)

        
2)

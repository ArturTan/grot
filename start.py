import grot

if __name__ == "__main__":
    
    side_length = int(input("What is side of your sample?:   "))
    sample, sample2 = sample_generator(side_length)
    o = range(len(sample[0]))
    chains = [] # here we put all chains that are in our sample
    grot_search = GrotSearcher(sample, chains, o)
    chains = grot_search.backend()
    
    max_lens = Viewer.max_lens(chains)
    Viewer.shower(max_lens, chains, sample2)

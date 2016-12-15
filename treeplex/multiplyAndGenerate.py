from decimal import Decimal
import sys
import os

def getSequencesWork(num_cards):
    return 14*num_cards+70*num_cards*num_cards

def getPayoffWork(num_cards):
    return 4*num_cards*num_cards + 45*num_cards*(num_cards*num_cards-1)

def getSampleWork(num_cards):
    sequences_touched = 84 #84 is the number of sequences touched per sample, for Leduc
    
    return 84;

def generateData(folder, a_multiplier, b_multiplier):
    for i in os.listdir(folder):
        new_file = open(folder + '_clean/' + i, 'w')
        min_value = 100000
        for line in open(folder+'/'+i):
            split_line = line.split('\t')
            num_cards = int(i.split('output')[1].split('card_leduc')[0])
            num_iterations = int(split_line[0])
            regret_max = Decimal(split_line[2])

            work_sequences = int(num_iterations * a_multiplier * getSequencesWork(num_cards))
            work_payoff = int(num_iterations * b_multiplier * getPayoffWork(num_cards))

            if regret_max < min_value:
                min_value = regret_max
            if(420000000 >= work_sequences + work_payoff):
                new_file.write(str(work_sequences + work_payoff) + '\t' +  str(min_value) + '\n')
            else:
                 break
        new_file.close()


def generateCFRData(folder):
    for i in os.listdir(folder):
        new_file = open(folder + '_clean/' + i, 'w')
        min_value = 100000
        for line in open(folder+'/'+i):
            split_line = line.split('\t')
            num_cards = int(i.split('output')[1].split('card_leduc')[0])
            num_iterations = int(split_line[0])
            regret_max = Decimal(split_line[2])
            work = int(split_line[5].split('\n')[0])

            if regret_max < min_value:
                min_value = regret_max
            if(420000000 >= work):
                new_file.write(str(work) + '\t' +  str(min_value) + '\n')
            else:
                 break
        new_file.close()

def generateSampleData(folder, c_multiplier):
    for i in os.listdir(folder):
        if "chance_samples=20.txt" not in i:
            continue
        print i
        new_file = open(folder + '_clean/' + i, 'w')
        min_value = 100000
        for line in open(folder+'/'+i):
            split_line = line.split('\t')
            num_cards = int(i.split('output')[1].split('card_leduc')[0])
            num_samples = int(i.split('chance_samples=')[1].split('.')[0])
            num_iterations = int(split_line[0])
            regret_max = Decimal(split_line[2])

            work = int(num_iterations * num_samples * c_multiplier * getSampleWork(num_cards))

            if regret_max < min_value:
                min_value = regret_max
            if(420000000 >= work):
                new_file.write(str(work) + '\t' +  str(min_value) + '\n')
            else:
                 break
        new_file.close()

#generateCFRData(sys.argv[1] + 'final_cfr_walk')
#generateData(sys.argv[1] + 'final_egt', 2.5, 3)
#generateData(sys.argv[1] + 'final_smp_deterministic', 5, 4)
#generateSampleData(sys.argv[1] + 'final_stochastic_smp', 5)
generateSampleData(sys.argv[1] + 'final_dayof_stochastic_smp', 5)


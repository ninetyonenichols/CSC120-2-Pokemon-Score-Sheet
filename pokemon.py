'''
File: pokemon.py
Author: Justin Nichols
Purpose: Reads in a CSV Pokemon data file, with one pokemon's data on
each line. Responds to user queries about which pokemon type has the highest
average value for each stat. These values are pre-computed ahead of time, so
that when the user is making queries, all that is needed is to look up the
appropriate values. Prints out the results
'''


def build_type_stats(num_ordr_stats):
    '''
    Purpose: creates a dictionary whose keys are pkmn types and whose
    values are
    lists of data, each corresponding to a pkmn within that type
    Arguments: num_ordr_stats, a list
    Return: type_stats, a dict
    '''    
    type_stats = {}
    
    for i in range(len(num_ordr_stats)):
        num_ordr_stats[i] = num_ordr_stats[i].strip().split(',')
        pkmn = num_ordr_stats[i]
        pkmn_stats = pkmn[4:11]
        for i in range(len(pkmn_stats)):
            pkmn_stats[i] = int(pkmn_stats[i])

        pkmn_type = pkmn[2]
        counter_index = (len(pkmn_stats))
        if pkmn_type not in type_stats.keys():
            type_stats[pkmn_type] = [0]*(counter_index +1)
    
        for i in range(len(pkmn_stats)):
            type_stats[pkmn_type][i] += pkmn_stats[i]
        type_stats[pkmn_type][counter_index] += 1

    for pkmn_type in type_stats.keys():
        for i in range(len(type_stats[pkmn_type]) - 1):
                stat_to_be_avgd = type_stats[pkmn_type][i]
         avg_stat = stat_to_be_avgd / type_stats[pkmn_type][counter_index]
                type_stats[pkmn_type][i] = avg_stat
        del type_stats[pkmn_type][counter_index]

    return type_stats


def build_vals_lists(stats_names, num_of_stats, strongest_type,
                     max_avgs, type_stats):
    '''
    Purpose: creates lists of values where the ith index of each list
    will be stored together in a tuple later for quick lookup
    Arguments: num_of_stats, and int
    Return: n/a
    '''
    for i in range(num_of_stats):
        for pkmn_type in type_stats.keys():     
            max_avg_candidate = type_stats[pkmn_type][i]

            if max_avg_candidate > max_avgs[i]:
                max_avgs[i] = max_avg_candidate
                strongest_type[i] = [pkmn_type]

            elif max_avg_candidate == max_avgs[i]:
                strongest_type[i].append(pkmn_type)
        strongest_type[i].sort()

        
def build_final_dict(stats_names, num_of_stats, strongest_type,
max_avgs):
    '''
 Purpose: builds the lookup table that will be used to answer queries
    Arguments: stats_names, a list. num_of stats, an int.
               strongest_type, a list. max_avgs, a list.
    Return: final_dict, a dict
    '''
    final_dict = {}
    for i in range(num_of_stats):
        final_dict[stats_names[i]] = (strongest_type[i], max_avgs[i])
    return final_dict


def process_query(final_dict):
    '''
    Purpose: responds to user queries about which type of pokemon
                 has the highest average stat, prints out each type
                 as well as the value for that stat
    Arguments: final_dict, a dict
    Return: n/a
    '''
    stat = input().lower()
    while stat != '':
        if stat in final_dict.keys():
            for one_type in final_dict[stat][0]:
                pokemon_type = one_type
                max_average = final_dict[stat][1]
        print("{}: {}".format(pokemon_type, max_average))
        stat = input()


def main():
    # getting the data file ready for processing
    pkmn_data_file = input()
    num_ordr_stats = open(pkmn_data_file).readlines()
    del num_ordr_stats[0]

    # building a dict whose keys are types and values are corresponding pkmn
    type_stats = build_type_stats(num_ordr_stats)
    
    # creating some lists that will be used to create the lookup dict later
    stats_names = ['total', 'hp', 'attack', 'defense', 'specialattack',
                       'specialdefense', 'speed']
    num_of_stats = len(stats_names)
    strongest_type = [[]]*num_of_stats
    max_avgs = [0]*num_of_stats
    build_vals_lists(stats_names, num_of_stats, strongest_type, max_avgs,
                         type_stats)

    # creating the lookup dict that will be used to answer queries
    final_dict = build_final_dict(stats_names, num_of_stats, strongest_type,
                                      max_avgs)

    # answering queries
    process_query(final_dict)


main()
            


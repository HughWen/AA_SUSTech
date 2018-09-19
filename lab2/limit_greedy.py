def limit_greedy(machine_num, t_list, specific_index, specific_machine_index, fold):
    makespan = 0
    assigns = [list() for i in range(machine_num)]
    accumulators = [0] * machine_num
    # assign specific joy to specific machine
    for index in sorted(specific_index, reverse=True):
        assigns[specific_machine_index].append(t_list[index])
        accumulators[specific_machine_index] += t_list[index]
        del t_list[index]
    # sort the task list
    t_list.sort(reverse=True)
    # assign job for machine
    for i in range(len(t_list)):
        min_value = min(accumulators)
        min_list = [j for j, x in enumerate(accumulators) if x == min_value]
        # if specific machine in minimum task time list, put the task to specific machine
        if specific_machine_index in min_list:
            assigns[specific_machine_index].append(t_list[i])
            accumulators[specific_machine_index] += t_list[i]
        # min_index = accumulators.index(min(accumulators))
        else:
            assigns[min_list[0]].append(t_list[i])
            accumulators[min_list[0]] += t_list[i] * fold
    makespan = max(accumulators)
    return makespan, assigns, accumulators

if __name__ == '__main__':
    m = 3
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    specific_index = [8, 9]
    specific_machine_index = 2
    fold = 2
    print(limit_greedy(m, t, specific_index, specific_machine_index, fold))

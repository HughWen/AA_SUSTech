def greedy_balance(machine_num, t_list, sort=False):
    # if "sort" is true, sort the time list.
    if sort:
        t_list.sort(reverse=True)
	# init
    makespan = 0
    assigns = [list() for i in range(machine_num)]
    accumulators = [0] * machine_num
	# assign job for machine
    for i in range(len(t_list)):
        min_index = accumulators.index(min(accumulators))
        assigns[min_index].append(t_list[i])
        accumulators[min_index] += t_list[i]

    makespan = max(accumulators)
    return makespan, assigns, accumulators


if __name__ == '__main__':
    m = 2
    t = [1, 1, 2]
    print(greedy_balance(m, t))
    print(greedy_balance(m, t, sort=True))
def greedy_solution(U, subset_list, cost_list):
    replace_zero = lambda x: x if x != 0 else 0.0001
    subset_select_list = []
    element_select_set = set()
    total_cost = 0
    while element_select_set != U:  
        unit_cost_list = [cost_list[i] / replace_zero(len(set(subset_list[i]) - element_select_set)) for i in range(len(subset_list))]
        best_subset_idx = unit_cost_list.index(min(unit_cost_list))
        subset_select_list.append(subset_list[best_subset_idx])
        element_select_set = element_select_set | set(subset_list[best_subset_idx])
        total_cost += cost_list[best_subset_idx]
    return subset_select_list, total_cost

if __name__ == '__main__':
    U = set([i for i in range(7)])
    subset_list = [[1, 3, 5], [2, 4, 6], [2, 0], [0, 1, 2, 3], [4, 5, 6]]
    cost_list = [1, 2, 3, 4, 5]
    subset_select_list, total_cost = greedy_solution(U, subset_list, cost_list)
    print(subset_select_list, total_cost)
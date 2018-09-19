class Machine():
    def __init__(self, limitation_task, efficiency):
        self.limitation_task = limitation_task
        self.efficiency = efficiency
        self.accumulator = 0
        self.task_list = []


def limit_greedy(machine_list, t_list):
    t_list.sort(reverse=True)
    for t in t_list:
        available_machine_list = [
            x for x in machine_list if t in x.limitation_task]
        min_accumu = min([m.accumulator for m in available_machine_list])
        m_list = [m for m in available_machine_list if m.accumulator == min_accumu]
        max_eff = max([m.efficiency for m in m_list])
        for m in m_list:
            if m.efficiency == max_eff:
                m.accumulator += t / m.efficiency
                m.task_list.append(t)
                break
    return max([m.accumulator for m in machine_list])


if __name__ == '__main__':
    m1 = Machine([i + 1 for i in range(7)], 0.5)
    m2 = Machine([i + 1 for i in range(8)], 0.5)
    m3 = Machine([i + 1 for i in range(10)], 1)
    max_accumulator = limit_greedy([m1, m2, m3], [i + 1 for i in range(10)])
    print(max_accumulator)
    print(m1.task_list, m1.accumulator)
    print(m2.task_list, m2.accumulator)
    print(m3.task_list, m3.accumulator)

def TowerOfHanoi(n, from_rod, to_rod, aux_rod, step_count):
    if n == 0:
        return step_count
    step_count = TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, step_count)
    step_count += 1
    print(f"Step {step_count}: Move disk {n} from rod {from_rod} to rod {to_rod}")
    step_count = TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, step_count)
    return step_count

# Driver code
N = 8  # You can change N to the desired number of disks

# A, C, B are the names of rods
TowerOfHanoi(N, 'A', 'C', 'B', 0)

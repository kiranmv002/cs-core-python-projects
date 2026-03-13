# Banker's Algorithm
# Operating Systems - Day 21
def calculate_need(max_matrix, allocation, p, r):

    need = []

    for i in range(p):
        row = []
        for j in range(r):
            row.append(max_matrix[i][j] - allocation[i][j])
        need.append(row)

    return need


def bankers_algorithm(p, r, allocation, max_matrix, available):

    need = calculate_need(max_matrix, allocation, p, r)

    finish = [False] * p
    safe_sequence = []

    work = available.copy()

    while len(safe_sequence) < p:

        found = False

        for i in range(p):

            if not finish[i]:

                possible = True

                for j in range(r):
                    if need[i][j] > work[j]:
                        possible = False
                        break

                if possible:

                    for j in range(r):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

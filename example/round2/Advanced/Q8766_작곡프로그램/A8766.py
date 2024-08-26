def is_valid(seq, banned, max_consec):
    # Check if the sequence contains any banned sequence
    for i in range(len(seq) - 1):
        if (seq[i], seq[i + 1]) in banned:
            return False

    # Check for consecutive major or minor chords
    major_count = 0
    minor_count = 0
    for chord in seq:
        if chord.endswith('m'):
            minor_count += 1
            major_count = 0
        else:
            major_count += 1
            minor_count = 0
        if major_count > max_consec or minor_count > max_consec:
            return False

    return True


def solution(banned_seqs, max_consec):
    chords = ["A", "B", "C", "D", "E", "F", "G", "Am", "Bm", "Cm", "Dm", "Em", "Fm", "Gm"]
    banned_set = set(tuple(seq.split()) for seq in banned_seqs)

    def backtrack(seq):
        if len(seq) == 5:
            return 1

        count = 0
        for chord in chords:
            if chord not in seq:
                seq.append(chord)
                if is_valid(seq, banned_set, max_consec):
                    count += backtrack(seq)
                seq.pop()
        return count

    return backtrack([])


if __name__ == "__main__":
    N, a = map(int, input().split())
    banned_seqs = [input().strip() for _ in range(N)]
    print(solution(banned_seqs, a))

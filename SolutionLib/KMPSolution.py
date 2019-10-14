def kmp(test_input):
    pat = test_input[0]
    txt = test_input[1]
    lps = compute_pattern_array(pat)
    pattern_size = len(pat)
    txt_size = len(txt)

    result = []
    pat_ptr = 0
    txt_ptr = 0
    while txt_ptr < txt_size:
        if txt[txt_ptr] == pat[pat_ptr]:
            txt_ptr += 1
            pat_ptr += 1

        if pat_ptr == pattern_size:
            result.append(txt_ptr-pat_ptr)
            pat_ptr = lps[pat_ptr-1]
        elif txt_ptr < txt_size and pat[pat_ptr] != txt[txt_ptr]:
            if pat_ptr != 0:
                pat_ptr = lps[pat_ptr-1]
            else:
                txt_ptr += 1
    print(result)


def compute_pattern_array(pattern):
    pattern_size = len(pattern)
    lps = [0] * pattern_size
    left_ptr = 0
    right_ptr = 1
    while right_ptr < pattern_size:
        if pattern[left_ptr] == pattern[right_ptr]:
            left_ptr += 1
            lps[right_ptr] = left_ptr
            right_ptr += 1
        else:
            if left_ptr == 0:
                lps[right_ptr] = 0 # not required
                right_ptr += 1
            else:
                left_ptr = lps[left_ptr-1]
    return lps


class KMPSolution:
    def __init__(self):
        self.solution = kmp

    def get_solution(self):
        if self.solution is None:
            raise Exception("No Solution Found")
        return self.solution

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def compare_automata(nfa1, nfa2):
    # Convert NFA to DFA using DFA.from_nfa()
    dfa1 = DFA.from_nfa(nfa1).minify()
    dfa2 = DFA.from_nfa(nfa2).minify()

    # Check for equivalence using the subset method
    if dfa1 <= dfa2 and dfa2 <= dfa1:
        return True, None
    else:
        # If they are not equivalent, find a counterexample
        return False, find_counterexample(dfa1, dfa2)


def find_counterexample(dfa1, dfa2):
    # Use symmetric difference to find the difference between DFA1 and DFA2
    diff_dfa = dfa1.symmetric_difference(dfa2)

    # Iterate through the DFA to find a word accepted by one but not the other
    for word in diff_dfa:
        return word
    return None


def main():
    # RE Input Section
    #n = 2
    #regex1 = "(b|ab)*"
    #regex2 = "((a|())bb*)*"
    #regexes = []
    #regexes.append(regex1)
    #regexes.append(regex2)

    # RE Input with Terminal
    n = int(input("Enter the number of regular expressions: "))
    regexes = [input(f"Enter regular expression {i + 1}: ") for i in range(n)]

    # Convert the regexes into NFAs
    automata = [NFA.from_regex(regex) for regex in regexes]

    # Compare each pair of automata
    for i in range(n):
        for j in range(i + 1, n):
            are_equal, counterexample = compare_automata(automata[i], automata[j])
            if are_equal:
                print(f"Regular expression {i + 1} is equivalent to {j + 1}.")
            else:
                print(f"Regular expression {i + 1} is NOT equivalent to {j + 1}. Counterexample: {counterexample}")


if __name__ == "__main__":
    main()

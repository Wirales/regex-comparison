# Regex Comparison Tool

A Python tool to compare two or more regular expressions for language equivalence by converting them into finite automata (NFA → DFA). If the regexes are not equivalent, it provides a counterexample that highlights the difference.

## Features

- Compares two or more regular expressions.
- Converts regexes into NFA → DFA using the `automata` library.
- Determines language equivalence.
- Provides a counterexample string if they differ.

## How It Works

1. Each regular expression is converted to an NFA.
2. NFAs are transformed into DFAs.
3. DFAs are minimized and then compared.
4. If not equivalent, a string accepted by one but rejected by the other is shown.

## Installation

```bash
git clone https://github.com/Wirales/regex-comparison.git
cd regex-comparison
pip install -r requirements.txt
```

Make sure the `automata-lib` is installed:

```bash
pip install automata-lib
```

## Example

```python
from regex_comparator import compare_regexes

regex1 = "(b|ab)*"
regex2 = "((a|())bb*)*"

result = compare_regexes(regex1, regex2)

if result['equivalent']:
    print("The regular expressions are equivalent.")
else:
    print("Not equivalent.")
    print("Counterexample:", result['counterexample'])
```

## To-Do / Ideas for Improvement

- Add a CLI interface (`argparse`)
- Add regex validation and informative error messages
- Support more robust counterexample generation
- Add automata visualization (e.g., Graphviz)
- Deploy as a small web app with Streamlit or Flask

## Contributions

Pull requests are welcome. If you have ideas or spot a bug, feel free to open an issue or submit a PR.

## License

MIT License

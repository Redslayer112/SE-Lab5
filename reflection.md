# Reflection

## 1. Which issues did the tools find that manual inspection could miss?

Bandit flagged the pickle load and the string-built SQL at once. Pylint found the shared mutable default `playlist=[]`. A quick read shows working output, so these defects stay hidden until a second call or hostile input exposes them.

## 2. Which tool gave the most useful findings?

Bandit gave the most serious findings, because it reported two Medium security issues. Pylint gave the widest coverage and a score. Flake8 reported only style, but its rules are strict and fast to apply.

## 3. Were there false positives or low-value findings?

The Low findings for the `pickle` import and for `random` need context. A music shuffle is not a security use. The change to `secrets.choice` costs nothing, so the fix stays. The docstring and naming messages improve readability but do not change behaviour.

## 4. How does static analysis change the development workflow?

The tools run in seconds and give a repeatable check before review. A team can run them in a commit hook or in continuous integration. Reviewers then spend time on logic instead of style. The tools do not replace tests, because they cannot prove that the program is correct.

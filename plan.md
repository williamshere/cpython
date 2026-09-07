1. **Analyze:** We identified `in [...]` lines in `Lib/turtle.py` that do O(N) lookup. Changing to `in {...}` allows the compiler to convert to a `frozenset` constant for O(1) lookups.
2. **Benchmark:** Use `timeit` to show the improvement of `in [...]` vs `in {...}`.
3. **Implement:** Update the line in `Lib/turtle.py:2150` as requested, and optionally other similar occurrences in the same file to be consistent and fully optimize.
4. **Verify:** Run turtle tests to ensure correctness.
5. **Pre-commit:** Run `pre_commit_instructions`.
6. **PR:** Submit the PR with the performance improvements.

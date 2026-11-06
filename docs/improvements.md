# Engineering improvements

### 2026-11-06 03:22 UTC — ChatGPT Portfolio Iteration
- Run ID: 20261106T032219Z-11
- Repo / Base SHA: 1998x-stack/X-LeetCode / c2faf56d65680b135bcb9407a24a11cd026221f4
- Historical context: First initialization; default-branch docs/improvements.md returned GitHub 404. No existing PRs were returned by repository PR search; last eight commits predate 2026.
- Product problem & expected user value: Re-running the problem scaffold must not destroy students' completed C++ answers or Markdown notes.
- Engineering diagnosis & evidence: utils.py LeetCodeDirectoryManager.create_file previously opened every path with mode 'w', truncating existing files. Directory creation with exist_ok=True makes repeated runs expected.
- Options & decision: (1) P0 existing-solution loss: benefit 5, correctness 5, evidence 5, verifiability 5, cost 1, risk 1 = 18; (2) P2 unknown level maps to Unknown: 3+2+4+4-2-2=9; (3) P2 Markdown link generation assumes solution files exist: 3+2+4+3-3-2=7. Choose the first, minimal behavior-preserving change for new files.
- Changes: utils.py uses exclusive creation ('x') and handles FileExistsError; tests/test_scaffold_safety.py covers existing C++ and Markdown preservation and new-file creation. Existing CLI, directory naming and template stay unchanged.
- Validation: A (isolated equivalent function): python /tmp/portfolio-test/test_guard.py -v, 4 tests passed, with test-harness ResourceWarnings. D (repository-integrated tests): python -m unittest discover -s tests -v not run against a complete checkout; no CI result claimed. C (static): source replacement verified exact previous code match.
- Security & regression review: No credentials, permissions, workflows, deployment or production data touched. Exclusive create is atomic and prevents truncation. Full repository test remains required.
- Risk & rollback: Existing files now remain untouched rather than regenerated, intentionally. Revert the two code/test commits on the feature branch if needed; do not merge until full regression.
- Follow-up: Run repository-integrated unittest suite and test simultaneous scaffold attempts in a clean checkout.
- Commit: e59639ca6682b3d4ebd840de86c6d7ac69568399 (test commit; history commit follows)
- PR: pending

# TECH-DEBT

<!--
The structural-health ledger. Feature tickets APPEND lines here (the architect lists this file
in the spec's Files to Modify, so code_review's diff-scope gate accepts it). Only the
`structural-health-<object>` analyzer REMOVES a line, and only after re-measuring the smell as
gone. Sorted by (path, smell) — sorting IS the grouping, so a refresh conflict stays a one-line
conflict.

The last column is the card id, or `—` when no card has been cut, or `wontfix`. Set
`wontfix` BY HAND when a heal card is closed without the code changing: the debt stays visible
and stops holding an in-flight slot. A `wontfix` line is still re-measured and still pruned once
its smell is gone; `wontfix` governs carding and counting only.
-->

<!-- tests-and-code report: re-measured weekly, do not edit by hand -->
tests-and-code: duplicates 0 groups, 0 lines
  excluded as generated: 596 files (manifest 1, marker 595)
tests-and-code: no_marginal_kill: no instrument (the built-in mutator runs only with the container runner)
tests-and-code: slow_tail: no instrument (no green full run on the base line with per-test seconds on record)
tests-and-code: copies 0 copies, 0 lines
  excluded as generated: 602 files (manifest 602, marker 0)
tests-and-code: dead_code 0 functions, 0 lines
  excluded as generated: 602 files (manifest 602, marker 0)
tests-and-code: co_failure: no instrument (no outcome source: this object's tests do not run through the test runner)
<!-- /tests-and-code report -->

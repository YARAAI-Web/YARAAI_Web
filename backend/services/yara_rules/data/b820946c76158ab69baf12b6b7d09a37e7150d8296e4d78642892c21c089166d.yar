rule auto_rule_20250726174002_9213 {
  strings:
    $o0 = "dwFlagsAndAttributes" wide ascii nocase
    $o1 = "dword_404428" wide ascii nocase
  condition:
    all of them
}
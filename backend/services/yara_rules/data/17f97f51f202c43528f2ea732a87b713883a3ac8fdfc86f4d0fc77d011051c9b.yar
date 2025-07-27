rule auto_rule_20250726232120_9669 {
  strings:
    $o0 = "__crtExitProcess" wide ascii nocase
    $o1 = "dword_42A008" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726130625_9435 {
  strings:
    $o0 = "dword_78D94" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}
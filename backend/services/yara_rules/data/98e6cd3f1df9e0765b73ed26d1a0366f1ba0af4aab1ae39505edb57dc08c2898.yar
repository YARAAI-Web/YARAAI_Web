rule auto_rule_20250726155052_3471 {
  strings:
    $o0 = "dword_477250" wide ascii nocase
  condition:
    all of them
}
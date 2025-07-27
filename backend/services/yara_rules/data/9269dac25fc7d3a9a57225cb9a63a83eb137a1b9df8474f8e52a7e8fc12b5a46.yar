rule auto_rule_20250726141931_6046 {
  strings:
    $o0 = "dword_4798F4" wide ascii nocase
    $o1 = "dword_479A14" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726164903_1560 {
  strings:
    $o0 = "dword_77F78" wide ascii nocase
    $o1 = "dword_78144" wide ascii nocase
  condition:
    all of them
}
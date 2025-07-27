rule auto_rule_20250726093032_4477 {
  strings:
    $o0 = "dword_44E5CC" wide ascii nocase
    $o1 = "dword_44E468" wide ascii nocase
  condition:
    all of them
}
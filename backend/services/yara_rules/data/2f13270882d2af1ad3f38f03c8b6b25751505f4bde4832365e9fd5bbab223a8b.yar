rule auto_rule_20250726153943_2736 {
  strings:
    $o0 = "dword_780E0" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}
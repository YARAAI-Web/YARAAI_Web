rule auto_rule_20250726222025_5424 {
  strings:
    $o0 = "dword_78418" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726133426_5134 {
  strings:
    $o0 = "dword_41158C" wide ascii nocase
  condition:
    all of them
}
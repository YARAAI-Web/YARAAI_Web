rule auto_rule_20250726123143_3120 {
  strings:
    $o0 = "_ioinit" wide ascii nocase
    $o1 = "dword_45A530" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726091424_9608 {
  strings:
    $o0 = "dword_780E4" wide ascii nocase
    $o1 = "dword_78150" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726084900_6141 {
  strings:
    $o0 = "dword_4173D4" wide ascii nocase
  condition:
    all of them
}
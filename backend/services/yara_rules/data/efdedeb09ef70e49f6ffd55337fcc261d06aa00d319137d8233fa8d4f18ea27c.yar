rule auto_rule_20250726095442_7532 {
  strings:
    $o0 = "dword_45B484" wide ascii nocase
    $o1 = "dword_45AFB0" wide ascii nocase
  condition:
    all of them
}
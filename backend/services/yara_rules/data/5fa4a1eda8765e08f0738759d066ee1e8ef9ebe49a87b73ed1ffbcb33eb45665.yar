rule auto_rule_20250726190323_2893 {
  strings:
    $o0 = "dword_42A008" wide ascii nocase
    $o1 = "dword_45C1C4" wide ascii nocase
  condition:
    all of them
}
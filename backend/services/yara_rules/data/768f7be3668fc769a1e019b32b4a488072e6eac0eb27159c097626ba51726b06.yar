rule auto_rule_20250726072740_5198 {
  strings:
    $o0 = "dword_45B498" wide ascii nocase
    $o1 = "dword_45AFDC" wide ascii nocase
    $o2 = "x403871" wide ascii nocase
    $o3 = "SetStdHandle" wide ascii nocase
    $o4 = "dword_45AFAC" wide ascii nocase
  condition:
    4 of ($o*)
}
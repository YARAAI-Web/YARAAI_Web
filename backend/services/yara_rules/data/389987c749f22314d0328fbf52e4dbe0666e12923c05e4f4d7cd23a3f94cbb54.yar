rule auto_rule_20250726070956_4173 {
  strings:
    $o0 = "C22h" wide ascii nocase
    $o1 = "x200002775LL" wide ascii nocase
    $o2 = "dword_4284E1" wide ascii nocase
  condition:
    3 of ($o*)
}
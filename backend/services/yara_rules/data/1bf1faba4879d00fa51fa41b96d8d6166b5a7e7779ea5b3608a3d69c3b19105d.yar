rule auto_rule_20250726151940_3827 {
  strings:
    $o0 = "nAtom" wide ascii nocase
    $o1 = "x399Eu" wide ascii nocase
    $o2 = "x3273u" wide ascii nocase
    $o3 = "dword_42D000" wide ascii nocase
  condition:
    4 of ($o*)
}
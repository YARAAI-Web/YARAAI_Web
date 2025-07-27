rule auto_rule_20250726123313_2497 {
  strings:
    $o0 = "fields" wide ascii nocase
    $o1 = "dword_469CE8" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
  condition:
    3 of ($o*)
}
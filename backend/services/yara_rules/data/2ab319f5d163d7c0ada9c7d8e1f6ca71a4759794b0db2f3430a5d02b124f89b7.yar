rule auto_rule_20250726181032_2389 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "TrailUp0_0" wide ascii nocase
    $o2 = "dword_445EAC" wide ascii nocase
  condition:
    3 of ($o*)
}
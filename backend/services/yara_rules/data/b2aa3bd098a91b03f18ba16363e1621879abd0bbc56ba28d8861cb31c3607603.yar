rule auto_rule_20250726181109_2450 {
  strings:
    $o0 = "TrailDown0_0" wide ascii nocase
    $o1 = "dword_42F028" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
  condition:
    3 of ($o*)
}
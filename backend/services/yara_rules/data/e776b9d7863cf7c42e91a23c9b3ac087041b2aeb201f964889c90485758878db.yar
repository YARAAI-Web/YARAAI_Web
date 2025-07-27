rule auto_rule_20250726122952_3559 {
  strings:
    $o0 = "dword_466A04" wide ascii nocase
    $o1 = "_NLG_Notify1" wide ascii nocase
    $o2 = "x38270" wide ascii nocase
    $o3 = "TrailUp3" wide ascii nocase
    $o4 = "x4134F5" wide ascii nocase
  condition:
    4 of ($o*)
}
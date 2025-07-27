rule auto_rule_20250727031026_2985 {
  strings:
    $o0 = "overrun" wide ascii nocase
    $o1 = "dword_45CF08" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
    $o3 = "x423CB5" wide ascii nocase
  condition:
    4 of ($o*)
}
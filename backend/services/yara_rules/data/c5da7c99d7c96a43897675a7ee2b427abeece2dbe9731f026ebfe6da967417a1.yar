rule auto_rule_20250727021634_4668 {
  strings:
    $o0 = "dword_44E824" wide ascii nocase
    $o1 = "x7FFFu" wide ascii nocase
    $o2 = "dword_44E1BC" wide ascii nocase
    $o3 = "TrailDown0_0" wide ascii nocase
    $o4 = "_allmul" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726201156_6348 {
  strings:
    $o0 = "off_44B820" wide ascii nocase
    $o1 = "UnwindUp4_0" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
    $o3 = "acmDriverClose" wide ascii nocase
    $o4 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}
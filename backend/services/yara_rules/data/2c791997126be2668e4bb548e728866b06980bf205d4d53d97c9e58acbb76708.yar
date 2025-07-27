rule auto_rule_20250726145359_6438 {
  strings:
    $o0 = "dword_4072A4" wide ascii nocase
    $o1 = "x56D1u" wide ascii nocase
    $o2 = "dword_4078B1" wide ascii nocase
    $o3 = "dword_407308" wide ascii nocase
    $o4 = "dword_4075CC" wide ascii nocase
  condition:
    4 of ($o*)
}
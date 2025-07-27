rule auto_rule_20250726132503_5905 {
  strings:
    $o0 = "dword_43B1A4" wide ascii nocase
    $o1 = "dword_43B7DF" wide ascii nocase
    $o2 = "x43636D00" wide ascii nocase
    $o3 = "dword_43B720" wide ascii nocase
    $o4 = "dword_43B5A2" wide ascii nocase
  condition:
    4 of ($o*)
}
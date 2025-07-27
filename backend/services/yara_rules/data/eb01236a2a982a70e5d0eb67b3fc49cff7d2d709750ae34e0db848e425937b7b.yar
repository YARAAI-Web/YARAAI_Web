rule auto_rule_20250726092838_0510 {
  strings:
    $o0 = "uUnique" wide ascii nocase
    $o1 = "off_42954F" wide ascii nocase
    $o2 = "dword_42A1CB" wide ascii nocase
    $o3 = "x37ECu" wide ascii nocase
  condition:
    4 of ($o*)
}
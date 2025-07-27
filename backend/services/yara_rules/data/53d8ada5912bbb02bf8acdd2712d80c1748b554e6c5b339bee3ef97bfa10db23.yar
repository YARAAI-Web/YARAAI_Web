rule auto_rule_20250726074435_7532 {
  strings:
    $o0 = "dword_449028" wide ascii nocase
    $o1 = "x12010u" wide ascii nocase
    $o2 = "off_44BBEC" wide ascii nocase
  condition:
    3 of ($o*)
}
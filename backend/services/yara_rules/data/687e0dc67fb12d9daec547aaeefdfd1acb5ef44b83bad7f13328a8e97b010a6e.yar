rule auto_rule_20250726200402_5303 {
  strings:
    $o0 = "dword_45A8F4" wide ascii nocase
    $o1 = "GetStringTypeA" wide ascii nocase
    $o2 = "off_45A1E8" wide ascii nocase
  condition:
    3 of ($o*)
}
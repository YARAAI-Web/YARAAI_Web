rule auto_rule_20250726092728_5802 {
  strings:
    $o0 = "dword_7811C" wide ascii nocase
    $o1 = "dword_781A4" wide ascii nocase
    $o2 = "sysa" wide ascii nocase
  condition:
    3 of ($o*)
}
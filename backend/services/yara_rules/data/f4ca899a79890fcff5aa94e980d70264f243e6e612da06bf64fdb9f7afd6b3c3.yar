rule auto_rule_20250726192152_7801 {
  strings:
    $o0 = "dword_14008D638" wide ascii nocase
    $o1 = "dword_14008D724" wide ascii nocase
    $o2 = "dword_14008D444" wide ascii nocase
  condition:
    3 of ($o*)
}
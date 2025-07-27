rule auto_rule_20250726230039_9471 {
  strings:
    $o0 = "dword_45D8AC" wide ascii nocase
    $o1 = "x4020B4" wide ascii nocase
    $o2 = "program" wide ascii nocase
  condition:
    3 of ($o*)
}
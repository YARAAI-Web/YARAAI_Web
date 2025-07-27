rule auto_rule_20250726205249_5901 {
  strings:
    $o0 = "dword_456F9C" wide ascii nocase
    $o1 = "atol" wide ascii nocase
    $o2 = "x3FFF" wide ascii nocase
  condition:
    3 of ($o*)
}
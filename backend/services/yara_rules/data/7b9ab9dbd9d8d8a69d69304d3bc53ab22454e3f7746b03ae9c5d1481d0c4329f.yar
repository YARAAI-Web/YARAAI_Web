rule auto_rule_20250726220128_5488 {
  strings:
    $o0 = "dword_467828" wide ascii nocase
    $o1 = "DrawDibDraw" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
  condition:
    3 of ($o*)
}
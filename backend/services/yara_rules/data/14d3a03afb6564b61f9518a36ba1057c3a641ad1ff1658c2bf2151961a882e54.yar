rule auto_rule_20250726091445_1501 {
  strings:
    $o0 = "x402C84" wide ascii nocase
    $o1 = "_ioinit" wide ascii nocase
    $o2 = "GetStringTypeA" wide ascii nocase
    $o3 = "dword_41198C" wide ascii nocase
    $o4 = "gu_return" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726184213_4698 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "x402C24" wide ascii nocase
    $o2 = "dword_412120" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
    $o4 = "dword_411D9C" wide ascii nocase
  condition:
    4 of ($o*)
}
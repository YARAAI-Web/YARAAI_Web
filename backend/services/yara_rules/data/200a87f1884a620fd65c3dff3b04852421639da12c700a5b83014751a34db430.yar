rule auto_rule_20250726212946_4775 {
  strings:
    $o0 = "dword_45D53C" wide ascii nocase
    $o1 = "dword_45D8AC" wide ascii nocase
    $o2 = "x402801" wide ascii nocase
    $o3 = "off_45CF40" wide ascii nocase
    $o4 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}
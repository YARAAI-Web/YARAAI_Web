rule auto_rule_20250726212200_5309 {
  strings:
    $o0 = "dword_46908C" wide ascii nocase
    $o1 = "byte_4691C1" wide ascii nocase
  condition:
    all of them
}
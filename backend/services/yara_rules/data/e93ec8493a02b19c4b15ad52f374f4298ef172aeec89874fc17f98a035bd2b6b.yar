rule auto_rule_20250726222456_1525 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "dword_41097C" wide ascii nocase
    $o2 = "byte_410B20" wide ascii nocase
    $o3 = "dword_410E64" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726151052_7259 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "off_476C48" wide ascii nocase
    $o2 = "dword_4727E8" wide ascii nocase
    $o3 = "dword_476E34" wide ascii nocase
  condition:
    4 of ($o*)
}
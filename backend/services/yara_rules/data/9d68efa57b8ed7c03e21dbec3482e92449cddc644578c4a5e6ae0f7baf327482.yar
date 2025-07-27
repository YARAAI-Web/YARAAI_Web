rule auto_rule_20250726184018_8399 {
  strings:
    $o0 = "dword_445020" wide ascii nocase
    $o1 = "dword_45FCC8" wide ascii nocase
    $o2 = "byte_45FE08" wide ascii nocase
  condition:
    3 of ($o*)
}
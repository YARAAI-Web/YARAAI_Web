rule auto_rule_20250726174246_7170 {
  strings:
    $o0 = "dword_445020" wide ascii nocase
    $o1 = "byte_45FE08" wide ascii nocase
    $o2 = "dword_460118" wide ascii nocase
  condition:
    3 of ($o*)
}
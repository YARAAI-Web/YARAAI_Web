rule auto_rule_20250727005101_1486 {
  strings:
    $o0 = "dword_476FAC" wide ascii nocase
    $o1 = "dword_476E80" wide ascii nocase
    $o2 = "byte_476C40" wide ascii nocase
  condition:
    3 of ($o*)
}
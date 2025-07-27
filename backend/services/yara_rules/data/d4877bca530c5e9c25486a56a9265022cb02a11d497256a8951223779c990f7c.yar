rule auto_rule_20250726081257_0878 {
  strings:
    $o0 = "byte_449EDC" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "GetStringTypeA" wide ascii nocase
    $o3 = "start_byte_3" wide ascii nocase
  condition:
    4 of ($o*)
}
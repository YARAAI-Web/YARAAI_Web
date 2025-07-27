rule auto_rule_20250727020152_8077 {
  strings:
    $o0 = "x10A3" wide ascii nocase
    $o1 = "x31F0u" wide ascii nocase
    $o2 = "x120Fu" wide ascii nocase
  condition:
    3 of ($o*)
}
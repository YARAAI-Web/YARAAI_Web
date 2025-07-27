rule auto_rule_20250726132257_4773 {
  strings:
    $o0 = "x7FFF" wide ascii nocase
    $o1 = "off_44D550" wide ascii nocase
    $o2 = "off_44DD18" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726062959_8834 {
  strings:
    $o0 = "byte_45CC14" wide ascii nocase
    $o1 = "_byte_0" wide ascii nocase
    $o2 = "Handler" wide ascii nocase
    $o3 = "GetLocaleInfoA" wide ascii nocase
  condition:
    4 of ($o*)
}
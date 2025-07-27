rule auto_rule_20250726113127_6861 {
  strings:
    $o0 = "byte_47DF20" wide ascii nocase
    $o1 = "GetLocaleInfoA" wide ascii nocase
  condition:
    all of them
}
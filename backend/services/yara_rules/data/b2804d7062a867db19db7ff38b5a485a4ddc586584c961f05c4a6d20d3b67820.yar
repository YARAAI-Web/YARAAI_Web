rule auto_rule_20250727035713_2973 {
  strings:
    $o0 = "dword_640303D4" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726142624_1294 {
  strings:
    $o0 = "write_multi_char" wide ascii nocase
    $o1 = "pUserData" wide ascii nocase
  condition:
    all of them
}
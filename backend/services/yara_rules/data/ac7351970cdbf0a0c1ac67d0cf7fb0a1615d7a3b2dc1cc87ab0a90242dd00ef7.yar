rule auto_rule_20250726162412_2508 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "off_4568AC" wide ascii nocase
  condition:
    all of them
}
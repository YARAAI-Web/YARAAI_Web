rule auto_rule_20250726235404_4418 {
  strings:
    $o0 = "extensions_cnt" wide ascii nocase
  condition:
    all of them
}
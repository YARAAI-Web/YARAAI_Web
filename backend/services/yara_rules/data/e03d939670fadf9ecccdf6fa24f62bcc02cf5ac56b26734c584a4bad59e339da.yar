rule auto_rule_20250726153724_1843 {
  strings:
    $o0 = "quarter" wide ascii nocase
    $o1 = "pclsidHandler" wide ascii nocase
  condition:
    all of them
}
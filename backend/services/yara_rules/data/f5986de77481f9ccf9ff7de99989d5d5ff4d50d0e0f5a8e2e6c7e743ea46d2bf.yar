rule auto_rule_20250726142432_8808 {
  strings:
    $o0 = "aPnguo61j" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}
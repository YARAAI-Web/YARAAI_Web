rule auto_rule_20250726194404_7081 {
  strings:
    $o0 = "x107A1F6C" wide ascii nocase
  condition:
    all of them
}
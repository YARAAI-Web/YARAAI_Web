rule auto_rule_20250726191152_6544 {
  strings:
    $o0 = "FatTime" wide ascii nocase
    $o1 = "enumRegFlags" wide ascii nocase
  condition:
    all of them
}
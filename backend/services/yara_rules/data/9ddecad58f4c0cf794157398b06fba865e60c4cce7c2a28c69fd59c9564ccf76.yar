rule auto_rule_20250726105518_1215 {
  strings:
    $o0 = "byte_640301F3" wide ascii nocase
  condition:
    all of them
}
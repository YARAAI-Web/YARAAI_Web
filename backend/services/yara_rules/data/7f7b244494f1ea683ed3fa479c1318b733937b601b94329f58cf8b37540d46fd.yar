rule auto_rule_20250726182441_3765 {
  strings:
    $o0 = "byte_64029040" wide ascii nocase
  condition:
    all of them
}
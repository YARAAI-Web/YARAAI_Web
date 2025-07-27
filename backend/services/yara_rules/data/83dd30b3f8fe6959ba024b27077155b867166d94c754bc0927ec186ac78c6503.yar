rule auto_rule_20250726213214_0013 {
  strings:
    $o0 = "byte_64029060" wide ascii nocase
  condition:
    all of them
}
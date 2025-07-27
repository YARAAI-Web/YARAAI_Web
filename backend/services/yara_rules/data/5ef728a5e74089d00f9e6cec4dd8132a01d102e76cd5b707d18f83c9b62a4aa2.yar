rule auto_rule_20250726062301_9007 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "byte_469BC4" wide ascii nocase
  condition:
    all of them
}
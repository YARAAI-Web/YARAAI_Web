rule auto_rule_20250726105053_0333 {
  strings:
    $o0 = "tionAndSpinCount" wide ascii nocase
    $o1 = "byte_45CC14" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726233851_6222 {
  strings:
    $o0 = "byte_40CD48" wide ascii nocase
  condition:
    all of them
}
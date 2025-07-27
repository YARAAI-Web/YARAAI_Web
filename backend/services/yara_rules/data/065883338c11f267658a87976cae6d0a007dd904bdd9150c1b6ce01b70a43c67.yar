rule auto_rule_20250726223626_1035 {
  strings:
    $o0 = "byte_640280B0" wide ascii nocase
  condition:
    all of them
}
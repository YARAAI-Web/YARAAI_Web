rule auto_rule_20250726223345_4614 {
  strings:
    $o0 = "byte_6402938C" wide ascii nocase
  condition:
    all of them
}
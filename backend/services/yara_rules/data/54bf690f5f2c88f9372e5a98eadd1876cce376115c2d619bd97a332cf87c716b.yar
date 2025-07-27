rule auto_rule_20250726131304_6434 {
  strings:
    $o0 = "byte_10004010" wide ascii nocase
  condition:
    all of them
}
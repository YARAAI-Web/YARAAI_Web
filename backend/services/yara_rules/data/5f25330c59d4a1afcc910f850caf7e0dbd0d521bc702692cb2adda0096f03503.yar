rule auto_rule_20250727011731_4023 {
  strings:
    $o0 = "pcbBytesNeeded" wide ascii nocase
    $o1 = "byte_64026616" wide ascii nocase
  condition:
    all of them
}
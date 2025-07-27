rule auto_rule_20250727013321_6900 {
  strings:
    $o0 = "lpFilename" wide ascii nocase
    $o1 = "byte_6ED9E7" wide ascii nocase
  condition:
    all of them
}
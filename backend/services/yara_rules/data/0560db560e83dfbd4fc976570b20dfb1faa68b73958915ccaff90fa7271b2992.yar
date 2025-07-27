rule auto_rule_20250727010900_7486 {
  strings:
    $o0 = "byte_64030190" wide ascii nocase
    $o1 = "dwErrCodec" wide ascii nocase
  condition:
    all of them
}
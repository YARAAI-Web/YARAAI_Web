rule auto_rule_20250726150639_6481 {
  strings:
    $o0 = "dword_4469D4" wide ascii nocase
    $o1 = "byte_446D00" wide ascii nocase
  condition:
    all of them
}
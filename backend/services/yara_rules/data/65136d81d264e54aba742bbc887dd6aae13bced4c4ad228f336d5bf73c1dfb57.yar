rule auto_rule_20250726102534_6397 {
  strings:
    $o0 = "byte_402201" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726154652_6828 {
  strings:
    $o0 = "byte_449600" wide ascii nocase
    $o1 = "ActiveWindow" wide ascii nocase
  condition:
    all of them
}
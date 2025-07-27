rule auto_rule_20250726172601_7817 {
  strings:
    $o0 = "CloseEventLog" wide ascii nocase
    $o1 = "byte_401EA9" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726103820_6655 {
  strings:
    $o0 = "ReadFmtUserTypeStg" wide ascii nocase
  condition:
    all of them
}
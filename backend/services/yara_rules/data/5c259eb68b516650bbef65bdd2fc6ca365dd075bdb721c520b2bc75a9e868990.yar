rule auto_rule_20250726215622_6765 {
  strings:
    $o0 = "off_418168" wide ascii nocase
    $o1 = "found_bx" wide ascii nocase
  condition:
    all of them
}
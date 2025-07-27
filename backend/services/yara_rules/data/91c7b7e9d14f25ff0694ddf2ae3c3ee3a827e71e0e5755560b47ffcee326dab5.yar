rule auto_rule_20250726210551_5299 {
  strings:
    $o0 = "byte_465D61" wide ascii nocase
    $o1 = "off_464634" wide ascii nocase
  condition:
    all of them
}
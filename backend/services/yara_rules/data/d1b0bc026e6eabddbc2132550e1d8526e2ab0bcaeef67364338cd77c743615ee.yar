rule auto_rule_20250727043507_6773 {
  strings:
    $o0 = "cause" wide ascii nocase
    $o1 = "off_446D40" wide ascii nocase
  condition:
    all of them
}
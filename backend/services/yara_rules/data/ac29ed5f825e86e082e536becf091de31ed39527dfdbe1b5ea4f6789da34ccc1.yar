rule auto_rule_20250726145228_4276 {
  strings:
    $o0 = "byte_4C1628" wide ascii nocase
    $o1 = "WinTextMatchMode" wide ascii nocase
  condition:
    all of them
}
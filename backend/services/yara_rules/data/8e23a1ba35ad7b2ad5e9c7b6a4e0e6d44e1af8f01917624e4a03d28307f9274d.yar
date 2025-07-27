rule auto_rule_20250726220654_8202 {
  strings:
    $o0 = "dwExceptionCode" wide ascii nocase
    $o1 = "x404E20" wide ascii nocase
  condition:
    all of them
}
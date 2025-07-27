rule auto_rule_20250726124051_4139 {
  strings:
    $o0 = "GetDIBits" wide ascii nocase
    $o1 = "x59D6" wide ascii nocase
  condition:
    all of them
}
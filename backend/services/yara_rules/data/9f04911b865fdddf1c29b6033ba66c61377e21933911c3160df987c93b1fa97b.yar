rule auto_rule_20250726191434_6911 {
  strings:
    $o0 = "vwprintf" wide ascii nocase
    $o1 = "FFF4h" wide ascii nocase
  condition:
    all of them
}
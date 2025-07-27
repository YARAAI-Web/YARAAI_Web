rule auto_rule_20250726160449_0417 {
  strings:
    $o0 = "FFF4h" wide ascii nocase
    $o1 = "x1D0" wide ascii nocase
  condition:
    all of them
}
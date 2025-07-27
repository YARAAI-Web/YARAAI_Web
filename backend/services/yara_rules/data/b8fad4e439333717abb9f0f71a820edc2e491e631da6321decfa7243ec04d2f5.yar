rule auto_rule_20250726132110_2321 {
  strings:
    $o0 = "cbInput" wide ascii nocase
    $o1 = "_cftoe2" wide ascii nocase
  condition:
    all of them
}
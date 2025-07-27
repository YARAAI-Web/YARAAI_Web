rule auto_rule_20250726224912_4780 {
  strings:
    $o0 = "dword_783BC" wide ascii nocase
  condition:
    all of them
}
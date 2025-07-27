rule auto_rule_20250726222645_3163 {
  strings:
    $o0 = "aGetlastactivep" wide ascii nocase
  condition:
    all of them
}
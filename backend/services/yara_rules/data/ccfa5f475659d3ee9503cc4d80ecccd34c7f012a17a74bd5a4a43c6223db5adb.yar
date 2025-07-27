rule auto_rule_20250726065426_2900 {
  strings:
    $o0 = "OnEraseBackground" wide ascii nocase
    $o1 = "_Mbstatet" wide ascii nocase
  condition:
    all of them
}
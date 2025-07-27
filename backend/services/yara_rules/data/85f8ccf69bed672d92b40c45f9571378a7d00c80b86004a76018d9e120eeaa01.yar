rule auto_rule_20250726182240_6637 {
  strings:
    $o0 = "var_1C8" wide ascii nocase
    $o1 = "var_208" wide ascii nocase
  condition:
    all of them
}
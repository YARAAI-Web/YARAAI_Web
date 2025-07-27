rule auto_rule_20250726080213_9066 {
  strings:
    $o0 = "x751084A" wide ascii nocase
  condition:
    all of them
}
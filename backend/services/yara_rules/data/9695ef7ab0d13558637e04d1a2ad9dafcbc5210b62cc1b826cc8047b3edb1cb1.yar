rule auto_rule_20250726202016_2492 {
  strings:
    $o0 = "AVIStreamCreate" wide ascii nocase
  condition:
    all of them
}
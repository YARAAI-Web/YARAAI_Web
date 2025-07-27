rule auto_rule_20250726211116_8480 {
  strings:
    $o0 = "gammadyne" wide ascii nocase
  condition:
    all of them
}
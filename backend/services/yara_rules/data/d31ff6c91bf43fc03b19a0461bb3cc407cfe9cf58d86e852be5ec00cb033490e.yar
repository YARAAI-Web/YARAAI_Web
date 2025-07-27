rule auto_rule_20250726165350_3850 {
  strings:
    $o0 = "uSize" wide ascii nocase
    $o1 = "off_418014" wide ascii nocase
  condition:
    all of them
}
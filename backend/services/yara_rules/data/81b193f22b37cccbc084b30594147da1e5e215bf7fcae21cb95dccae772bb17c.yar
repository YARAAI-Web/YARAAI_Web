rule auto_rule_20250726232721_9385 {
  strings:
    $o0 = "hUser" wide ascii nocase
    $o1 = "TabbedTextOutW" wide ascii nocase
  condition:
    all of them
}
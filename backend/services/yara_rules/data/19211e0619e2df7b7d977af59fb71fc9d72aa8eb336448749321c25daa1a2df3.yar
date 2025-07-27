rule auto_rule_20250726095527_1275 {
  strings:
    $o0 = "szUserMessage" wide ascii nocase
  condition:
    all of them
}
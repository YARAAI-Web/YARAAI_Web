rule auto_rule_20250726112211_9696 {
  strings:
    $o0 = "byte_423924" wide ascii nocase
  condition:
    all of them
}
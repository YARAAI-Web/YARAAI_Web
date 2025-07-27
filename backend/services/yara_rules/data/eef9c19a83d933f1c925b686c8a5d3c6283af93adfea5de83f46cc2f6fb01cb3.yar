rule auto_rule_20250726150625_5431 {
  strings:
    $o0 = "dword_10098EEC" wide ascii nocase
  condition:
    all of them
}
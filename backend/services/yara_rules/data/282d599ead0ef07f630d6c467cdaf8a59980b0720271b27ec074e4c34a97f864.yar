rule auto_rule_20250727004242_9889 {
  strings:
    $o0 = "dword_100D35E8" wide ascii nocase
  condition:
    all of them
}
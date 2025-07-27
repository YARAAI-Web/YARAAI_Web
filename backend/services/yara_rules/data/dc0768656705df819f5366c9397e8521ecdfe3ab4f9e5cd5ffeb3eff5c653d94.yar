rule auto_rule_20250727001017_9503 {
  strings:
    $o0 = "dword_7F794" wide ascii nocase
  condition:
    all of them
}
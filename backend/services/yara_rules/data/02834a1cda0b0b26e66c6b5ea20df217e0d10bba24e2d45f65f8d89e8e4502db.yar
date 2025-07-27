rule auto_rule_20250727012145_6668 {
  strings:
    $o0 = "dword_10066E04" wide ascii nocase
  condition:
    all of them
}
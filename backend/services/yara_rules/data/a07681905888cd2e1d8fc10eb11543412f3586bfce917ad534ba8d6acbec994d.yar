rule auto_rule_20250727024145_2456 {
  strings:
    $o0 = "dword_64030370" wide ascii nocase
  condition:
    all of them
}
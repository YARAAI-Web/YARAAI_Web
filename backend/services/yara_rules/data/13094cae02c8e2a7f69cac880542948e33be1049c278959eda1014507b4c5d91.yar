rule auto_rule_20250727044842_3211 {
  strings:
    $o0 = "dword_4D016C" wide ascii nocase
  condition:
    all of them
}
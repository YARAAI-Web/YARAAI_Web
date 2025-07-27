rule auto_rule_20250727005959_3138 {
  strings:
    $o0 = "dword_467760" wide ascii nocase
    $o1 = "_itoa" wide ascii nocase
  condition:
    all of them
}
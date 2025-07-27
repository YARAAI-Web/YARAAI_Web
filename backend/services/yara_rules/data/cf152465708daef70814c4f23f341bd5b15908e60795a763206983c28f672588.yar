rule auto_rule_20250727041746_0994 {
  strings:
    $o0 = "dword_503618" wide ascii nocase
  condition:
    all of them
}
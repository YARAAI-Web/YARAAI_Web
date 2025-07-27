rule auto_rule_20250727040452_1281 {
  strings:
    $o0 = "dword_427E98" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250727040511_0473 {
  strings:
    $o0 = "dword_2AA01148" wide ascii nocase
  condition:
    all of them
}
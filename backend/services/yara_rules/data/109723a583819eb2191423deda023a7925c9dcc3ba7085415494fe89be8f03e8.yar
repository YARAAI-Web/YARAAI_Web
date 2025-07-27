rule auto_rule_20250727034114_1867 {
  strings:
    $o0 = "aProgid" wide ascii nocase
    $o1 = "dword_4184C8" wide ascii nocase
  condition:
    all of them
}
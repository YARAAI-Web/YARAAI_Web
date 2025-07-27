rule auto_rule_20250727011257_6721 {
  strings:
    $o0 = "dword_401888" wide ascii nocase
    $o1 = "dword_40BADC" wide ascii nocase
  condition:
    all of them
}
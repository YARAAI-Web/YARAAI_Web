rule auto_rule_20250727025257_2302 {
  strings:
    $o0 = "dword_4C1680" wide ascii nocase
    $o1 = "dword_4C15F0" wide ascii nocase
  condition:
    all of them
}
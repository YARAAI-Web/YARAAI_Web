rule auto_rule_20250727025504_1833 {
  strings:
    $o0 = "dword_44C140" wide ascii nocase
    $o1 = "dword_44BE7C" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250727035440_8876 {
  strings:
    $o0 = "dword_455A04" wide ascii nocase
    $o1 = "CodePagea" wide ascii nocase
  condition:
    all of them
}
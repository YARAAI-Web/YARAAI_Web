rule auto_rule_20250727025727_8605 {
  strings:
    $o0 = "dword_6402C3F8" wide ascii nocase
    $o1 = "lpvReserved" wide ascii nocase
  condition:
    all of them
}
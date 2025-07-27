rule auto_rule_20250727004037_3643 {
  strings:
    $o0 = "byte_4BB568" wide ascii nocase
    $o1 = "dword_4C1684" wide ascii nocase
  condition:
    all of them
}
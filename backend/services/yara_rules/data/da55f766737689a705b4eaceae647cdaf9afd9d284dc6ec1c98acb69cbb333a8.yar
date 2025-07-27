rule auto_rule_20250727033514_8172 {
  strings:
    $o0 = "byte_4C1712" wide ascii nocase
    $o1 = "dword_4C12A0" wide ascii nocase
  condition:
    all of them
}
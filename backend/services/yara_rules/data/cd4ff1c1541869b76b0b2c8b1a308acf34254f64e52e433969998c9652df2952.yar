rule auto_rule_20250727035545_2755 {
  strings:
    $o0 = "dword_4C1784" wide ascii nocase
    $o1 = "dword_4C1698" wide ascii nocase
  condition:
    all of them
}
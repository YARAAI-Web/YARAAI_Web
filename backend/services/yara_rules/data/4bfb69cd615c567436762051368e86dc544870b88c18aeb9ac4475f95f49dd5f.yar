rule auto_rule_20250727035844_7244 {
  strings:
    $o0 = "dword_7830C" wide ascii nocase
    $o1 = "dword_1E8DC" wide ascii nocase
  condition:
    all of them
}
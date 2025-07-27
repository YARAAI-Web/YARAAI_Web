rule auto_rule_20250727035649_7310 {
  strings:
    $o0 = "fill_dwords_with_EOS" wide ascii nocase
    $o1 = "dword_411960" wide ascii nocase
  condition:
    all of them
}
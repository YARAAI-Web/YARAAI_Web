rule auto_rule_20250726094120_1773 {
  strings:
    $o0 = "dword_40ED50" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
  condition:
    all of them
}
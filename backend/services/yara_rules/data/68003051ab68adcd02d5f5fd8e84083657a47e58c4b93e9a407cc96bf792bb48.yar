rule auto_rule_20250727010820_4646 {
  strings:
    $o0 = "dword_440404" wide ascii nocase
    $o1 = "main_loop_2" wide ascii nocase
    $o2 = "dword_43D018" wide ascii nocase
    $o3 = "fill_dwords_with_EOS" wide ascii nocase
  condition:
    4 of ($o*)
}
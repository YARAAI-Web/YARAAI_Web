rule auto_rule_20250727044400_5115 {
  strings:
    $o0 = "dword_478784" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
    $o2 = "off_478178" wide ascii nocase
  condition:
    3 of ($o*)
}
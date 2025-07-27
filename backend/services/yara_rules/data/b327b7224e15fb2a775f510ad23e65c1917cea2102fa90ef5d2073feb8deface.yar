rule auto_rule_20250727005626_2465 {
  strings:
    $o0 = "dword_445ABC" wide ascii nocase
    $o1 = "dword_446044" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    3 of ($o*)
}
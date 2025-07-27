rule auto_rule_20250727004003_8379 {
  strings:
    $o0 = "dword_449A88" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    3 of ($o*)
}
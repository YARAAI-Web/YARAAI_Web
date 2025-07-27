rule auto_rule_20250726174625_0881 {
  strings:
    $o0 = "fill_dwords_with_EOS" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "dword_44B7C0" wide ascii nocase
  condition:
    3 of ($o*)
}
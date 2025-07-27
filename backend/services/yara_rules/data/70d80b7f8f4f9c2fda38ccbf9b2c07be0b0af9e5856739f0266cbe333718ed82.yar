rule auto_rule_20250726121615_0274 {
  strings:
    $o0 = "ActiveWindow_0" wide ascii nocase
    $o1 = "dword_45D3C4" wide ascii nocase
    $o2 = "fill_dwords_with_EOS" wide ascii nocase
    $o3 = "byte_45D3EC" wide ascii nocase
  condition:
    4 of ($o*)
}
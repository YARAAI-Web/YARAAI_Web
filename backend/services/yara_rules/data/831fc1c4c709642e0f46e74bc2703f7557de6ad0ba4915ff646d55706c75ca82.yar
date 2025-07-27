rule auto_rule_20250726112524_9870 {
  strings:
    $o0 = "fill_dwords_with_EOS" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
    $o2 = "dword_40E9C8" wide ascii nocase
    $o3 = "dword_40EB2C" wide ascii nocase
    $o4 = "tail_loop_start" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726061103_9560 {
  strings:
    $o0 = "main_loop_start" wide ascii nocase
    $o1 = "dword_45D260" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
    $o3 = "_NLG_Notify" wide ascii nocase
  condition:
    4 of ($o*)
}
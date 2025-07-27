rule auto_rule_20250726210627_9968 {
  strings:
    $o0 = "dword_44A010" wide ascii nocase
    $o1 = "dword_449EC4" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
    $o4 = "_except_handler3" wide ascii nocase
  condition:
    4 of ($o*)
}
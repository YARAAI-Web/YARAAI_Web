rule auto_rule_20250726165104_8199 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_449AB4" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    3 of ($o*)
}
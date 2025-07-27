rule auto_rule_20250726175718_9871 {
  strings:
    $o0 = "strpbrk" wide ascii nocase
    $o1 = "_ShrMan" wide ascii nocase
    $o2 = "dword_457A48" wide ascii nocase
    $o3 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    4 of ($o*)
}
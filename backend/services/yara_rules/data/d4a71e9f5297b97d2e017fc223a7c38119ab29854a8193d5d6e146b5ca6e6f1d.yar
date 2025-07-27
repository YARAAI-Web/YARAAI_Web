rule auto_rule_20250726083416_8617 {
  strings:
    $o0 = "dword_40B01C" wide ascii nocase
    $o1 = "dword_449FF0" wide ascii nocase
    $o2 = "dword_44A06C" wide ascii nocase
    $o3 = "_nh_malloc" wide ascii nocase
  condition:
    4 of ($o*)
}
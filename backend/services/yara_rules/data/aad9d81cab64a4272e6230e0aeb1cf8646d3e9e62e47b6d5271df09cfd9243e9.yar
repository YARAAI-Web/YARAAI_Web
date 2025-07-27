rule auto_rule_20250726101510_2392 {
  strings:
    $o0 = "dword_42A861" wide ascii nocase
    $o1 = "dword_42A781" wide ascii nocase
    $o2 = "dword_42A895" wide ascii nocase
    $o3 = "GetMapMode" wide ascii nocase
  condition:
    4 of ($o*)
}
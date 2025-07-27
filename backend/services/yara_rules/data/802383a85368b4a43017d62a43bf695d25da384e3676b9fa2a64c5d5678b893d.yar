rule auto_rule_20250726090559_1041 {
  strings:
    $o0 = "dword_411588" wide ascii nocase
    $o1 = "dword_411E48" wide ascii nocase
    $o2 = "_cpinfo" wide ascii nocase
    $o3 = "strncnt" wide ascii nocase
    $o4 = "dword_40E020" wide ascii nocase
  condition:
    4 of ($o*)
}
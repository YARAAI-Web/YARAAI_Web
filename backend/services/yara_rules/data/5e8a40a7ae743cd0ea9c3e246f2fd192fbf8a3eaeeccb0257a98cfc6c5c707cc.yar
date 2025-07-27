rule auto_rule_20250726071733_2267 {
  strings:
    $o0 = "dword_466AD4" wide ascii nocase
    $o1 = "dword_466D40" wide ascii nocase
    $o2 = "VirtualFree" wide ascii nocase
    $o3 = "dword_468334" wide ascii nocase
    $o4 = "dword_466910" wide ascii nocase
  condition:
    4 of ($o*)
}
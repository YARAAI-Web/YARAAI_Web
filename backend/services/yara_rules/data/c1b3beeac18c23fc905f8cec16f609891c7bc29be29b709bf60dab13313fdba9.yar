rule auto_rule_20250726152252_1785 {
  strings:
    $o0 = "_forcdecpt" wide ascii nocase
    $o1 = "off_427540" wide ascii nocase
    $o2 = "dword_4275CC" wide ascii nocase
    $o3 = "dword_427CD0" wide ascii nocase
    $o4 = "_heap_init" wide ascii nocase
  condition:
    4 of ($o*)
}
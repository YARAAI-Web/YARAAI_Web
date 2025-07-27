rule auto_rule_20250726220425_2174 {
  strings:
    $o0 = "dword_479624" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "_onexit_lk" wide ascii nocase
  condition:
    4 of ($o*)
}
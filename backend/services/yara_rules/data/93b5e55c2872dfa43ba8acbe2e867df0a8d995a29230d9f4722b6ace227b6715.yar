rule auto_rule_20250726082340_7679 {
  strings:
    $o0 = "dword_411E4C" wide ascii nocase
    $o1 = "dword_411978" wide ascii nocase
    $o2 = "dword_40E004" wide ascii nocase
    $o3 = "dword_411E50" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}
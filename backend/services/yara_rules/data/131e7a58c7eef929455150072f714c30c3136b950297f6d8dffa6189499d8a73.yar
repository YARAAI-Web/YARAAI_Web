rule auto_rule_20250726092635_9837 {
  strings:
    $o0 = "dword_4C2240" wide ascii nocase
    $o1 = "_ioinit" wide ascii nocase
    $o2 = "aAtan_0" wide ascii nocase
    $o3 = "dword_48D8AC" wide ascii nocase
    $o4 = "_forcdecpt_l" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726092638_5119 {
  strings:
    $o0 = "start_6" wide ascii nocase
    $o1 = "_cfltcvt" wide ascii nocase
    $o2 = "off_4BADA4" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726092642_6216 {
  condition:
    auto_rule_20250726092635_9837 or auto_rule_20250726092638_5119
}
rule auto_rule_20250726212757_7216 {
  strings:
    $o0 = "tail_loop_start_0" wide ascii nocase
    $o1 = "__freetlocinfo" wide ascii nocase
    $o2 = "dword_45DB00" wide ascii nocase
    $o3 = "off_45D91C" wide ascii nocase
    $o4 = "byte_45DF21" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726212757_0735 {
  strings:
    $o0 = "_except_handler3" wide ascii nocase
    $o1 = "off_45D908" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726212802_1891 {
  condition:
    auto_rule_20250726212757_7216 or auto_rule_20250726212757_0735
}
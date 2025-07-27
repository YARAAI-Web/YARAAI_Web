rule auto_rule_20250726071007_1320 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "mixerSetControlDetails" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
    $o3 = "off_411500" wide ascii nocase
    $o4 = "dword_4119B0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726071010_2267 {
  strings:
    $o0 = "off_4115B4" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726071013_0106 {
  condition:
    auto_rule_20250726071007_1320 or auto_rule_20250726071010_2267
}
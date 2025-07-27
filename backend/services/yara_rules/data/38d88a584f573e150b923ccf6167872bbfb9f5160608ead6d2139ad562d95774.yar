rule auto_rule_20250726132717_3496 {
  strings:
    $o0 = "dword_460784" wide ascii nocase
    $o1 = "dword_46062C" wide ascii nocase
    $o2 = "dword_4605FC" wide ascii nocase
    $o3 = "_cinit" wide ascii nocase
    $o4 = "dword_45FE0C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726132720_7812 {
  strings:
    $o0 = "x_ismbbtype" wide ascii nocase
    $o1 = "dword_45FE08" wide ascii nocase
    $o2 = "main_loop_entrance_0" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726132723_1290 {
  condition:
    auto_rule_20250726132717_3496 or auto_rule_20250726132720_7812
}
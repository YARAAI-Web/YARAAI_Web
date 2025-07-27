rule auto_rule_20250726100407_5060 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
    $o2 = "dword_40BE54" wide ascii nocase
    $o3 = "x_ismbbtype" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726212012_6540 {
  strings:
    $o0 = "_ms_p5_mp_test_fdiv" wide ascii nocase
    $o1 = "_ShrMan" wide ascii nocase
    $o2 = "dword_455E80" wide ascii nocase
    $o3 = "off_45647C" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726143945_1415 {
  strings:
    $o0 = "x480u" wide ascii nocase
    $o1 = "program" wide ascii nocase
    $o2 = "dword_44E5D0" wide ascii nocase
    $o3 = "_ms_p5_mp_test_fdiv" wide ascii nocase
    $o4 = "GdipCreateFontFamilyFromName" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726143948_9061 {
  strings:
    $o0 = "dword_44E44C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726143958_9641 {
  condition:
    auto_rule_20250726143945_1415 or auto_rule_20250726143948_9061
}
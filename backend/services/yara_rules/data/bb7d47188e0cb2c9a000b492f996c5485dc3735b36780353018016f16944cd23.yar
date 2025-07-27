rule auto_rule_20250726203120_8538 {
  strings:
    $o0 = "xA15" wide ascii nocase
    $o1 = "wParam_4b" wide ascii nocase
    $o2 = "dword_42C735" wide ascii nocase
    $o3 = "dword_42C8B5" wide ascii nocase
    $o4 = "x600" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726203123_3415 {
  strings:
    $o0 = "x19EB00001034LL" wide ascii nocase
    $o1 = "x1E8Bu" wide ascii nocase
    $o2 = "x6E7Du" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726203129_1200 {
  condition:
    auto_rule_20250726203120_8538 or auto_rule_20250726203123_3415
}
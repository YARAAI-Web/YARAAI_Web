rule auto_rule_20250726154444_7772 {
  strings:
    $o0 = "dword_45D3F0" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
    $o2 = "dword_45D3F4" wide ascii nocase
    $o3 = "dword_45D3C8" wide ascii nocase
    $o4 = "waveInClose" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726154447_2508 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "dword_45D54C" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726154451_3981 {
  condition:
    auto_rule_20250726154444_7772 or auto_rule_20250726154447_2508
}
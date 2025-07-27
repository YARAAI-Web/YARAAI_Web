rule auto_rule_20250726124503_3625 {
  strings:
    $o0 = "dword_411504" wide ascii nocase
    $o1 = "_except_handler3" wide ascii nocase
    $o2 = "dword_40E018" wide ascii nocase
    $o3 = "byte_411B20" wide ascii nocase
    $o4 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726124506_2390 {
  strings:
    $o0 = "dword_411AF0" wide ascii nocase
    $o1 = "dword_40E000" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726124509_8837 {
  condition:
    auto_rule_20250726124503_3625 or auto_rule_20250726124506_2390
}
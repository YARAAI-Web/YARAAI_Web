rule auto_rule_20250726181921_4166 {
  strings:
    $o0 = "x19DCC" wide ascii nocase
    $o1 = "x774E" wide ascii nocase
    $o2 = "dword_40F544" wide ascii nocase
    $o3 = "x61A5u" wide ascii nocase
    $o4 = "x7185u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726181925_7807 {
  strings:
    $o0 = "xFFFFFA49" wide ascii nocase
    $o1 = "dword_40F56C" wide ascii nocase
    $o2 = "dword_40F36C" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726181929_4861 {
  condition:
    auto_rule_20250726181921_4166 or auto_rule_20250726181925_7807
}
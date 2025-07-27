rule auto_rule_20250726061701_4119 {
  strings:
    $o0 = "dword_43B8AE" wide ascii nocase
    $o1 = "x54AFDE00" wide ascii nocase
    $o2 = "dword_43B5CC" wide ascii nocase
    $o3 = "dword_43B14D" wide ascii nocase
    $o4 = "dword_43B3F2" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726061704_9064 {
  strings:
    $o0 = "a58Rtmfzwnxtlll" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726061709_2286 {
  condition:
    auto_rule_20250726061701_4119 or auto_rule_20250726061704_9064
}
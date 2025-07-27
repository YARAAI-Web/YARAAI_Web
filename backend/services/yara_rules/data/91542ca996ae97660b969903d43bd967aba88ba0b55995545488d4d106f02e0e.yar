rule auto_rule_20250726170642_0790 {
  strings:
    $o0 = "dword_45D508" wide ascii nocase
    $o1 = "dword_45D3E4" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "dword_45D3C8" wide ascii nocase
    $o4 = "dword_45D500" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726170645_1897 {
  strings:
    $o0 = "dword_45D554" wide ascii nocase
    $o1 = "RtlUnwind" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726170648_0241 {
  condition:
    auto_rule_20250726170642_0790 or auto_rule_20250726170645_1897
}
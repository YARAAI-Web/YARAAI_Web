rule auto_rule_20250726124941_4903 {
  strings:
    $o0 = "TrailUp3" wide ascii nocase
    $o1 = "off_45CF40" wide ascii nocase
    $o2 = "xFF000000" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
    $o4 = "dword_45D3F4" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726124944_2661 {
  strings:
    $o0 = "dword_45D57C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726124948_9813 {
  condition:
    auto_rule_20250726124941_4903 or auto_rule_20250726124944_2661
}
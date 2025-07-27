rule auto_rule_20250726085759_6248 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "dword_443F14" wide ascii nocase
    $o2 = "ActiveWindow" wide ascii nocase
    $o3 = "off_4431D4" wide ascii nocase
    $o4 = "_msize" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726085802_9370 {
  strings:
    $o0 = "dword_443AF8" wide ascii nocase
    $o1 = "__sbh_alloc_new_region" wide ascii nocase
    $o2 = "dodwords" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726085805_5977 {
  condition:
    auto_rule_20250726085759_6248 or auto_rule_20250726085802_9370
}
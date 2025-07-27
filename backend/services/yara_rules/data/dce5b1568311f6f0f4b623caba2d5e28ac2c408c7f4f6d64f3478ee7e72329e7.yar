rule auto_rule_20250726190720_6296 {
  strings:
    $o0 = "lSize" wide ascii nocase
    $o1 = "atol" wide ascii nocase
    $o2 = "dword_44C6C4" wide ascii nocase
    $o3 = "VirtualFree" wide ascii nocase
    $o4 = "off_44BB0C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726190723_6564 {
  strings:
    $o0 = "dword_44C2F0" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726190727_8320 {
  condition:
    auto_rule_20250726190720_6296 or auto_rule_20250726190723_6564
}
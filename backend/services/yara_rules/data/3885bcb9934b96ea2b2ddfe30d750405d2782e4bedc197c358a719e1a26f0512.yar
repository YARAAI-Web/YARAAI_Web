rule auto_rule_20250726212829_6719 {
  strings:
    $o0 = "VirtualProtectEx" wide ascii nocase
    $o1 = "dword_45FFE8" wide ascii nocase
    $o2 = "off_45FA14" wide ascii nocase
    $o3 = "dword_45FEB4" wide ascii nocase
    $o4 = "dword_45FFEC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726212832_7239 {
  strings:
    $o0 = "byte_45F518" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726212836_1753 {
  condition:
    auto_rule_20250726212829_6719 or auto_rule_20250726212832_7239
}
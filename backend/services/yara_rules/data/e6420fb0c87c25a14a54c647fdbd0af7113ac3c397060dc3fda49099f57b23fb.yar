rule auto_rule_20250726165138_0891 {
  strings:
    $o0 = "x1004u" wide ascii nocase
    $o1 = "CopyUnwindUp_0" wide ascii nocase
    $o2 = "dword_45CB00" wide ascii nocase
    $o3 = "dword_45C430" wide ascii nocase
    $o4 = "_nh_malloc" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726165141_8992 {
  strings:
    $o0 = "dword_45CDA4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726165146_6912 {
  condition:
    auto_rule_20250726165138_0891 or auto_rule_20250726165141_8992
}
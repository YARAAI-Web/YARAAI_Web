rule auto_rule_20250726192855_7925 {
  strings:
    $o0 = "dword_45D57C" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "dword_45D8A4" wide ascii nocase
    $o3 = "LibraryA" wide ascii nocase
    $o4 = "strncnt" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726192858_4157 {
  strings:
    $o0 = "dword_45D500" wide ascii nocase
    $o1 = "dword_45D3C0" wide ascii nocase
    $o2 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726192902_9749 {
  condition:
    auto_rule_20250726192855_7925 or auto_rule_20250726192858_4157
}
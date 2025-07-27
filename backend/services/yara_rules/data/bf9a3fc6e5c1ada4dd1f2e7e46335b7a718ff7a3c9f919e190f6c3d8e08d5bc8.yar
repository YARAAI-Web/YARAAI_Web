rule auto_rule_20250726181535_2496 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "dword_45D3B8" wide ascii nocase
    $o3 = "dword_45D504" wide ascii nocase
    $o4 = "dword_45D3F4" wide ascii nocase
  condition:
    4 of ($o*)
}
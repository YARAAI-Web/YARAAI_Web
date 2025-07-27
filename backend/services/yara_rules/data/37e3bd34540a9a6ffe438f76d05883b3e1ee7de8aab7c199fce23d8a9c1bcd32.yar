rule auto_rule_20250726201134_7289 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "byte_4766BC" wide ascii nocase
    $o3 = "__heap_select" wide ascii nocase
    $o4 = "dword_475FF0" wide ascii nocase
  condition:
    4 of ($o*)
}
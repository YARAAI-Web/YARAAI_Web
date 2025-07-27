rule auto_rule_20250726095750_8624 {
  strings:
    $o0 = "dword_45AA20" wide ascii nocase
    $o1 = "_filbuf" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "SrcSizeInBytes" wide ascii nocase
  condition:
    4 of ($o*)
}
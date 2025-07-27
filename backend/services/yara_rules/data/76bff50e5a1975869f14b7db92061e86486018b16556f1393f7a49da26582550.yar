rule auto_rule_20250726203631_3866 {
  strings:
    $o0 = "dword_45D3B8" wide ascii nocase
    $o1 = "TrailUp3" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
    $o3 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}
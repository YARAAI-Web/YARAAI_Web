rule auto_rule_20250726065638_2938 {
  strings:
    $o0 = "dword_411904" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "Runtime" wide ascii nocase
    $o3 = "TrailDown0_0" wide ascii nocase
    $o4 = "byte_40F994" wide ascii nocase
  condition:
    4 of ($o*)
}
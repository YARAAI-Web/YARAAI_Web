rule auto_rule_20250726230326_0173 {
  strings:
    $o0 = "xcptlookup" wide ascii nocase
    $o1 = "GetStringTypeW" wide ascii nocase
    $o2 = "dword_40E018" wide ascii nocase
    $o3 = "xFF000000" wide ascii nocase
    $o4 = "dword_411970" wide ascii nocase
  condition:
    5 of ($o*)
}
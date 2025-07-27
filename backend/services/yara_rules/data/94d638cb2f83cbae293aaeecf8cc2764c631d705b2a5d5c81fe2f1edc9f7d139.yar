rule auto_rule_20250726061211_5930 {
  strings:
    $o0 = "DefaultChar" wide ascii nocase
    $o1 = "x7F28" wide ascii nocase
    $o2 = "SetCommTimeouts" wide ascii nocase
    $o3 = "off_421C86" wide ascii nocase
    $o4 = "AddAtomA" wide ascii nocase
  condition:
    4 of ($o*)
}
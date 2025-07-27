rule auto_rule_20250726235206_6254 {
  strings:
    $o0 = "szFile" wide ascii nocase
    $o1 = "dwResSize" wide ascii nocase
    $o2 = "IsCharAlphaA" wide ascii nocase
    $o3 = "SetComputerNameExW" wide ascii nocase
  condition:
    4 of ($o*)
}
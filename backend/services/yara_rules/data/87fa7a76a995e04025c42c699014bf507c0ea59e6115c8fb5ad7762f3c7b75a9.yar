rule auto_rule_20250726162336_5031 {
  strings:
    $o0 = "hWndNewParent" wide ascii nocase
    $o1 = "CreateIconFromResource" wide ascii nocase
    $o2 = "pwszBuff" wide ascii nocase
    $o3 = "GetKeyNameTextA" wide ascii nocase
  condition:
    4 of ($o*)
}
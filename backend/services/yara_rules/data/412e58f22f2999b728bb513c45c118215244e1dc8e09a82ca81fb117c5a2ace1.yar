rule auto_rule_20250726140237_1388 {
  strings:
    $o0 = "x56D1" wide ascii nocase
    $o1 = "x43F7" wide ascii nocase
    $o2 = "ScaleWindowExtEx" wide ascii nocase
    $o3 = "PageSetupDlgW" wide ascii nocase
  condition:
    4 of ($o*)
}
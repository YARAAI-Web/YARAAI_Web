rule auto_rule_20250726223302_3296 {
  strings:
    $o0 = "pSIRequested" wide ascii nocase
    $o1 = "puiHi" wide ascii nocase
    $o2 = "pszItemText" wide ascii nocase
    $o3 = "lpmii" wide ascii nocase
  condition:
    4 of ($o*)
}
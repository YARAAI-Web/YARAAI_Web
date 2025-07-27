rule auto_rule_20250726100846_8452 {
  strings:
    $o0 = "lpszSection" wide ascii nocase
    $o1 = "ulOptions" wide ascii nocase
    $o2 = "pimldp" wide ascii nocase
    $o3 = "xRight" wide ascii nocase
    $o4 = "CreateCursor" wide ascii nocase
  condition:
    4 of ($o*)
}
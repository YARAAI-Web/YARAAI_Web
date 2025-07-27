rule auto_rule_20250726073538_3673 {
  strings:
    $o0 = "nTabOrigin" wide ascii nocase
    $o1 = "SwapMouseButton" wide ascii nocase
    $o2 = "uIDItem" wide ascii nocase
    $o3 = "DdeConnectList" wide ascii nocase
  condition:
    4 of ($o*)
}
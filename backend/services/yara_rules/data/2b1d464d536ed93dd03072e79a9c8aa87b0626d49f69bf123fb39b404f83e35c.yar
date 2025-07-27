rule auto_rule_20250726073647_9883 {
  strings:
    $o0 = "bMenu" wide ascii nocase
    $o1 = "dword_420B60" wide ascii nocase
    $o2 = "GetStockObject" wide ascii nocase
    $o3 = "SetROP2" wide ascii nocase
    $o4 = "lstrlenW" wide ascii nocase
  condition:
    5 of ($o*)
}
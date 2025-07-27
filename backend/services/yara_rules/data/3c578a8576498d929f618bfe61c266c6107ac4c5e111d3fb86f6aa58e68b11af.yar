rule auto_rule_20250726174549_9046 {
  strings:
    $o0 = "lpLastWriteTime" wide ascii nocase
    $o1 = "BuildCommDCBW" wide ascii nocase
    $o2 = "DdeEnableCallback" wide ascii nocase
    $o3 = "FoldStringA" wide ascii nocase
  condition:
    4 of ($o*)
}
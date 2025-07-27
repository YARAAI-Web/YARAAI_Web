rule auto_rule_20250726233025_2514 {
  strings:
    $o0 = "lpszSrc" wide ascii nocase
    $o1 = "cchOut" wide ascii nocase
    $o2 = "hUserHandle" wide ascii nocase
    $o3 = "dwFlagsAndAttributes" wide ascii nocase
    $o4 = "DdeUninitialize" wide ascii nocase
  condition:
    4 of ($o*)
}
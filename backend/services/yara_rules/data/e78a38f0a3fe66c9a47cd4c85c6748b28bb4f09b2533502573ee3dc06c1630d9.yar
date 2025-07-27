rule auto_rule_20250726100825_5070 {
  strings:
    $o0 = "WindowFromDC" wide ascii nocase
    $o1 = "idAttach" wide ascii nocase
    $o2 = "pfnFilterProc" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726231410_2841 {
  strings:
    $o0 = "aNdvnnn32" wide ascii nocase
    $o1 = "lpOverlapped" wide ascii nocase
  condition:
    all of them
}
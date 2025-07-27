rule auto_rule_20250726115804_8281 {
  strings:
    $o0 = "dword_412374" wide ascii nocase
    $o1 = "hWinPosInfo" wide ascii nocase
  condition:
    all of them
}
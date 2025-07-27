rule auto_rule_20250726220747_8383 {
  strings:
    $o0 = "dword_4647D0" wide ascii nocase
    $o1 = "_cinit" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726100605_8189 {
  strings:
    $o0 = "x8C9D" wide ascii nocase
    $o1 = "x869F" wide ascii nocase
    $o2 = "x26F9" wide ascii nocase
    $o3 = "dword_4346CF" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726125039_6841 {
  strings:
    $o0 = "x3FD0u" wide ascii nocase
    $o1 = "nBitCount" wide ascii nocase
    $o2 = "dword_43372B" wide ascii nocase
    $o3 = "hDesktop" wide ascii nocase
  condition:
    4 of ($o*)
}
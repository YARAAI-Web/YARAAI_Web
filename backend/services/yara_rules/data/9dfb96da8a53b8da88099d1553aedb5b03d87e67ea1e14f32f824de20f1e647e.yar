rule auto_rule_20250726093210_3460 {
  strings:
    $o0 = "dword_42A9BD" wide ascii nocase
    $o1 = "x2A37" wide ascii nocase
    $o2 = "dword_41EB62" wide ascii nocase
    $o3 = "x7A0D5426" wide ascii nocase
    $o4 = "x751C80u" wide ascii nocase
  condition:
    4 of ($o*)
}
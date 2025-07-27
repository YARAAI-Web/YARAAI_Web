rule auto_rule_20250726144749_0813 {
  strings:
    $o0 = "FileAttributes" wide ascii nocase
    $o1 = "dword_42A008" wide ascii nocase
    $o2 = "dword_42B000" wide ascii nocase
    $o3 = "dword_429018" wide ascii nocase
    $o4 = "x2EB5u" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726125759_6502 {
  strings:
    $o0 = "ptScreen" wide ascii nocase
    $o1 = "ExeNameBuffer" wide ascii nocase
    $o2 = "LoadCursorFromFileA" wide ascii nocase
    $o3 = "pstm" wide ascii nocase
    $o4 = "ReuseDDElParam" wide ascii nocase
  condition:
    4 of ($o*)
}
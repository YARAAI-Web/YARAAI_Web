rule auto_rule_20250726115446_3590 {
  strings:
    $o0 = "dword_45618C" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "dword_456210" wide ascii nocase
    $o3 = "VisualC" wide ascii nocase
    $o4 = "__ascii_strnicmp" wide ascii nocase
  condition:
    4 of ($o*)
}
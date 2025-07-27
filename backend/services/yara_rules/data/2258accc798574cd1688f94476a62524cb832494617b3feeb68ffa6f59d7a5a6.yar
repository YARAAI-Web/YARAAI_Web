rule auto_rule_20250726181627_7889 {
  strings:
    $o0 = "_forcdecpt" wide ascii nocase
    $o1 = "off_4564AC" wide ascii nocase
    $o2 = "UnwindUp6_0" wide ascii nocase
    $o3 = "_mtdeletelocks" wide ascii nocase
    $o4 = "dword_456930" wide ascii nocase
  condition:
    4 of ($o*)
}
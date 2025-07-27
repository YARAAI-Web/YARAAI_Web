rule auto_rule_20250726201031_6126 {
  strings:
    $o0 = "NewFilePointer" wide ascii nocase
    $o1 = "dword_4C1160" wide ascii nocase
    $o2 = "dword_4C10F4" wide ascii nocase
    $o3 = "GUIDataSeparatorChar" wide ascii nocase
    $o4 = "dword_4C1280" wide ascii nocase
  condition:
    4 of ($o*)
}
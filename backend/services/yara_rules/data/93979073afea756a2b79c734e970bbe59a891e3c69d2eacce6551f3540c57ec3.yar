rule auto_rule_20250726181207_3768 {
  strings:
    $o0 = "dword_41DB30" wide ascii nocase
    $o1 = "nMaxPos" wide ascii nocase
    $o2 = "nIDComboBox" wide ascii nocase
    $o3 = "GetWindowModuleFileNameA" wide ascii nocase
    $o4 = "a1oftware" wide ascii nocase
  condition:
    4 of ($o*)
}
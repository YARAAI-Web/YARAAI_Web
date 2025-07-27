rule auto_rule_20250726101117_1698 {
  strings:
    $o0 = "dword_1E6B0" wide ascii nocase
    $o1 = "dword_781E8" wide ascii nocase
    $o2 = "ZwQueryInformationThread" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}
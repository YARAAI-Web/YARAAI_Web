rule auto_rule_20250726191724_6196 {
  strings:
    $o0 = "VirtualAllocEx" wide ascii nocase
    $o1 = "dword_4012D8" wide ascii nocase
    $o2 = "RegOpenKeyA" wide ascii nocase
    $o3 = "EFFh" wide ascii nocase
  condition:
    4 of ($o*)
}
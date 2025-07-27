rule auto_rule_20250726162951_7496 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "dword_464278" wide ascii nocase
    $o2 = "UsedDefaultChar" wide ascii nocase
    $o3 = "FlushFileBuffers" wide ascii nocase
  condition:
    4 of ($o*)
}
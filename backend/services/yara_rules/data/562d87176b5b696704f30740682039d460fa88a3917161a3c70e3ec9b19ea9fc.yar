rule auto_rule_20250726150713_9601 {
  strings:
    $o0 = "dword_409020" wide ascii nocase
    $o1 = "dword_40E988" wide ascii nocase
    $o2 = "_abnormal_termination" wide ascii nocase
    $o3 = "byte_40EB40" wide ascii nocase
  condition:
    4 of ($o*)
}
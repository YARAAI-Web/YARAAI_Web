rule auto_rule_20250726173720_9899 {
  strings:
    $o0 = "VariantChangeType" wide ascii nocase
    $o1 = "ResumeHandle" wide ascii nocase
    $o2 = "dword_6402F190" wide ascii nocase
  condition:
    3 of ($o*)
}
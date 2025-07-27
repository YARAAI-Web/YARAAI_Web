rule auto_rule_20250726171103_2713 {
  strings:
    $o0 = "dword_7F7EC" wide ascii nocase
    $o1 = "dword_7ED74" wide ascii nocase
    $o2 = "KeAttachProcess" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}
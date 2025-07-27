rule auto_rule_20250726110626_9395 {
  strings:
    $o0 = "_c_exit" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "dword_473008" wide ascii nocase
    $o3 = "UnwindUp1_0" wide ascii nocase
  condition:
    4 of ($o*)
}
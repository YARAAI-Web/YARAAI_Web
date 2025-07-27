rule auto_rule_20250726055756_1824 {
  strings:
    $o0 = "_CopyMan" wide ascii nocase
    $o1 = "tionAndSpinCount" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "dword_466020" wide ascii nocase
  condition:
    4 of ($o*)
}
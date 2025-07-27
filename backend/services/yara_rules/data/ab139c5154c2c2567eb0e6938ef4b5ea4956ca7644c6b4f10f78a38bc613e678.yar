rule auto_rule_20250726222404_9903 {
  strings:
    $o0 = "__endstdio" wide ascii nocase
    $o1 = "dword_460614" wide ascii nocase
    $o2 = "fflush" wide ascii nocase
    $o3 = "_global_unwind2" wide ascii nocase
  condition:
    4 of ($o*)
}
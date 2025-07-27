rule auto_rule_20250727010113_9697 {
  strings:
    $o0 = "dword_7822C" wide ascii nocase
    $o1 = "dword_775B8" wide ascii nocase
    $o2 = "KeGetCurrentIrql" wide ascii nocase
    $o3 = "kbdq" wide ascii nocase
  condition:
    4 of ($o*)
}
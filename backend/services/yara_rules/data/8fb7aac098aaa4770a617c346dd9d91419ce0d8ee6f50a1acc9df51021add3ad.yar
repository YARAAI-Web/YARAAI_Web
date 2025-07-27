rule auto_rule_20250726081529_6594 {
  strings:
    $o0 = "dword_45D268" wide ascii nocase
    $o1 = "dword_45C440" wide ascii nocase
    $o2 = "_mtdeletelocks" wide ascii nocase
    $o3 = "_global_unwind2" wide ascii nocase
  condition:
    4 of ($o*)
}
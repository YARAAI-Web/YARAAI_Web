rule auto_rule_20250727032610_9064 {
  strings:
    $o0 = "_heap_alloc" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "dword_45D8B0" wide ascii nocase
    $o3 = "dword_450020" wide ascii nocase
  condition:
    4 of ($o*)
}
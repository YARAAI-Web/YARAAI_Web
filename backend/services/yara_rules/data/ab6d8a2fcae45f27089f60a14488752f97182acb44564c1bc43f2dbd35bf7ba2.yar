rule auto_rule_20250726135012_9643 {
  strings:
    $o0 = "_cpinfo" wide ascii nocase
    $o1 = "_heap_alloc" wide ascii nocase
    $o2 = "__crtMessageBoxA" wide ascii nocase
    $o3 = "VirtualFree" wide ascii nocase
    $o4 = "dword_449948" wide ascii nocase
  condition:
    5 of ($o*)
}
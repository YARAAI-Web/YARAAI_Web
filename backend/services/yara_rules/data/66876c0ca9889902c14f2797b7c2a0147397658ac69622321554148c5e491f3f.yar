rule auto_rule_20250727035248_5599 {
  strings:
    $o0 = "dword_4118F0" wide ascii nocase
    $o1 = "OpenMutexA" wide ascii nocase
    $o2 = "finish_loop" wide ascii nocase
    $o3 = "LibraryA" wide ascii nocase
    $o4 = "__crtMessageBoxA" wide ascii nocase
  condition:
    4 of ($o*)
}
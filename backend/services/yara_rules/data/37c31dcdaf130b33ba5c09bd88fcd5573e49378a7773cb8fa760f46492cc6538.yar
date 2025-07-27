rule auto_rule_20250726130138_8897 {
  strings:
    $o0 = "_CrtIsValidHeapPointer" wide ascii nocase
    $o1 = "dword_469548" wide ascii nocase
    $o2 = "finish_loop" wide ascii nocase
    $o3 = "x157" wide ascii nocase
  condition:
    4 of ($o*)
}
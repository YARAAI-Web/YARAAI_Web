rule auto_rule_20250726073828_7657 {
  strings:
    $o0 = "dword_4674E0" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "_CrtIsValidHeapPointer" wide ascii nocase
    $o3 = "off_46750C" wide ascii nocase
    $o4 = "dword_4673E8" wide ascii nocase
  condition:
    4 of ($o*)
}
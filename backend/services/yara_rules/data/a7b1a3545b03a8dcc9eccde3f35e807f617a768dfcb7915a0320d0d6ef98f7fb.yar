rule auto_rule_20250726084923_8138 {
  strings:
    $o0 = "xF89C853E" wide ascii nocase
    $o1 = "dword_433727" wide ascii nocase
    $o2 = "lpProc" wide ascii nocase
    $o3 = "dword_433827" wide ascii nocase
  condition:
    4 of ($o*)
}